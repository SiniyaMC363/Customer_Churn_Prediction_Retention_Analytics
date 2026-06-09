from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import pickle
import os
from datetime import datetime
from uuid import uuid4

# Load model, encoders, and scaler
with open('best_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)
with open('encoder.pkl', 'rb') as encoders_file:
    encoders = pickle.load(encoders_file)
with open('scaler.pkl', 'rb') as scaler_file:
    scaler_data = pickle.load(scaler_file)

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'churn-analytics-dev-key-change-in-production')

DASHBOARD_IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.webp', '.gif'}
MAX_PREDICTION_HISTORY = 10


def get_risk_category(probability):
    pct = probability * 100
    if pct < 35:
        return 'Low Risk', 'low', pct
    if pct < 65:
        return 'Medium Risk', 'medium', pct
    return 'High Risk', 'high', pct


def make_prediction(input_data):
    input_df = pd.DataFrame([input_data])

    for col, encoder in encoders.items():
        input_df[col] = encoder.transform(input_df[col])

    numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    input_df[numerical_cols] = scaler_data.transform(input_df[numerical_cols])

    prediction = loaded_model.predict(input_df)[0]
    probability = loaded_model.predict_proba(input_df)[0, 1]
    status = 'Churn' if prediction == 1 else 'No Churn'
    risk_label, risk_level, risk_pct = get_risk_category(probability)
    return status, probability, risk_label, risk_level, risk_pct


def parse_form_data(form):
    return {
        'gender': form['gender'],
        'SeniorCitizen': int(form['SeniorCitizen']),
        'Partner': form['Partner'],
        'Dependents': form['Dependents'],
        'tenure': int(form['tenure']),
        'PhoneService': form['PhoneService'],
        'MultipleLines': form['MultipleLines'],
        'InternetService': form['InternetService'],
        'OnlineSecurity': form['OnlineSecurity'],
        'OnlineBackup': form['OnlineBackup'],
        'DeviceProtection': form['DeviceProtection'],
        'TechSupport': form['TechSupport'],
        'StreamingTV': form['StreamingTV'],
        'StreamingMovies': form['StreamingMovies'],
        'Contract': form['Contract'],
        'PaperlessBilling': form['PaperlessBilling'],
        'PaymentMethod': form['PaymentMethod'],
        'MonthlyCharges': float(form['MonthlyCharges']),
        'TotalCharges': float(form['TotalCharges']),
    }


def add_to_prediction_history(entry):
    history = session.get('prediction_history', [])
    history.insert(0, entry)
    session['prediction_history'] = history[:MAX_PREDICTION_HISTORY]


def get_dashboard_images():
    dashboard_dir = os.path.join(app.static_folder, 'dashboard')
    if not os.path.isdir(dashboard_dir):
        return []

    images = []
    for filename in sorted(os.listdir(dashboard_dir)):
        _, ext = os.path.splitext(filename.lower())
        if ext in DASHBOARD_IMAGE_EXTENSIONS:
            images.append({
                'filename': filename,
                'title': os.path.splitext(filename)[0].replace('_', ' ').replace('-', ' ').title(),
            })
    return images


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        input_data = parse_form_data(request.form)
        status, probability, risk_label, risk_level, risk_pct = make_prediction(input_data)

        result = {
            'id': str(uuid4())[:8],
            'timestamp': datetime.now().strftime('%b %d, %Y · %I:%M %p'),
            'status': status,
            'probability': round(probability * 100, 1),
            'risk_label': risk_label,
            'risk_level': risk_level,
            'risk_pct': round(risk_pct, 1),
            'customer': {
                'gender': input_data['gender'],
                'tenure': input_data['tenure'],
                'contract': input_data['Contract'],
                'monthly_charges': input_data['MonthlyCharges'],
                'internet_service': input_data['InternetService'],
            },
        }

        session['latest_prediction'] = result
        add_to_prediction_history(result)
        return redirect(url_for('result'))

    return render_template('predict.html')


@app.route('/result')
def result():
    prediction = session.get('latest_prediction')
    history = session.get('prediction_history', [])
    return render_template('result.html', prediction=prediction, history=history)


@app.route('/dashboard')
def dashboard():
    images = get_dashboard_images()
    return render_template('dashboard.html', dashboard_images=images)


if __name__ == '__main__':
    app.run(debug=True)
