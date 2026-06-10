# Customer Churn Prediction and Retention Analytics Platform

## Project Overview

Customer churn is a major challenge for subscription-based businesses, as losing customers directly impacts revenue and growth. This project is an end-to-end Machine Learning and Business Intelligence application designed to predict customers who are likely to leave a service and provide actionable insights for improving customer retention.

The application combines Machine Learning, Flask web development, SQL database management, and Power BI analytics to create a professional customer retention intelligence platform.

---

## Problem Statement

Businesses need to identify customers who are at risk of leaving before churn happens. The goal of this project is to analyze customer behavior, predict churn probability, classify customer risk levels, and provide data-driven retention strategies.

---

## Key Features

### Customer Churn Prediction

* Predicts whether a customer is likely to churn using a trained Machine Learning model.
* Displays churn probability score.
* Categorizes customers into Low, Medium, and High-risk groups.
* Provides personalized retention recommendations.

### Professional Web Application

* Modern responsive user interface built using HTML, CSS, Bootstrap, and JavaScript.
* Dedicated pages for:

  * Home page
  * Customer prediction form
  * Prediction result analysis
  * Analytics dashboard

### Machine Learning Pipeline

* Data preprocessing and cleaning.
* Exploratory Data Analysis (EDA).
* Feature engineering.
* Multiple model training and comparison:

  * Logistic Regression
  * Decision Tree Classifier
  * Random Forest Classifier
* Model evaluation using:

  * Accuracy
  * Precision
  * Recall
  * F1-Score
  * ROC-AUC Score
* Final model saved using Pickle (`model.pkl`).

### Database Integration

* Stores customer prediction history in MySQL.
* Maintains information such as:

  * Customer details
  * Prediction result
  * Churn probability
  * Risk category
  * Prediction timestamp

### Business Intelligence Dashboard

* Interactive Power BI dashboard for business users.
* Visualizes:

  * Customer churn rate
  * Customer segmentation
  * High-risk customer distribution
  * Revenue-related insights
  * Customer behavior patterns

---

## Technology Stack

### Programming & Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn

### Web Development

* Flask
* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Database

* MySQL

### Data Visualization & Analytics

* Power BI

### Version Control

* Git & GitHub

---

## Project Architecture

```
Customer Data
       |
       v
Data Cleaning & Feature Engineering
       |
       v
Machine Learning Model Training
       |
       v
Saved Model (model.pkl)
       |
       v
Flask Backend API
       |
       v
Responsive Web Application
       |
       v
MySQL Database Storage
       |
       v
Power BI Analytics Dashboard
```

---

## Application Pages

### 1. Home Page

Provides an introduction to the project, business problem, key features, and technology stack.

### 2. Customer Prediction Page

Allows users to enter customer information and request a churn prediction.

### 3. Prediction Result Page

Displays:

* Churn prediction outcome.
* Probability percentage.
* Customer risk category.
* Retention recommendations.

### 4. Analytics Dashboard

Displays Power BI visualizations to monitor churn trends, customer segments, and business KPIs.

---

## Machine Learning Workflow

1. Data Collection and Understanding.
2. Data Cleaning and Preprocessing.
3. Exploratory Data Analysis (EDA).
4. Feature Engineering.
5. Data Encoding and Transformation.
6. Model Training and Hyperparameter Optimization.
7. Model Evaluation and Selection.
8. Model Serialization using Pickle.
9. Deployment using Flask.

---

## Project Folder Structure

```
customer_churn_prediction/
│
├── dataset/
│   └── Telco_Customer_Churn.csv
│
├── notebooks/
│   └── churn_prediction.ipynb
│
├── model/
│   ├── model.pkl
│   ├── encoder.pkl
│   └── scaler.pkl
│
├── templates/
│   ├── index.html
│   ├── predict.html
│   ├── result.html
│   └── dashboard.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│
├── database/
│   └── schema.sql
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation and Setup

### Clone the Repository

```bash
git clone <repository-url>
cd customer_churn_prediction
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## Future Enhancements

* Deploy the application using cloud platforms.
* Add user authentication and role-based access.
* Implement real-time customer monitoring.
* Integrate automated email retention campaigns.
* Improve model performance using advanced algorithms.

---

## Business Impact

This project helps organizations proactively identify customers at risk of leaving, understand major churn factors, and make data-driven decisions to improve customer retention and customer lifetime value.

---

## Author

**Siniya MC**

AI & Data Science Graduate
Machine Learning | Data Analytics | Business Intelligence

GitHub: https://github.com/SiniyaMC363
LinkedIn: https://www.linkedin.com/in/siniya-mc
