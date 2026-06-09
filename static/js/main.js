document.addEventListener('DOMContentLoaded', () => {
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');

    document.querySelectorAll('.dashboard-item img').forEach((img) => {
        img.addEventListener('click', () => {
            if (!lightbox || !lightboxImg) return;
            lightboxImg.src = img.src;
            lightbox.classList.add('active');
        });
    });

    if (lightbox) {
        lightbox.addEventListener('click', () => {
            lightbox.classList.remove('active');
            if (lightboxImg) lightboxImg.src = '';
        });
    }

    const ring = document.querySelector('.probability-ring .ring-fill');
    if (ring) {
        const circumference = 2 * Math.PI * 70;
        const pct = parseFloat(ring.dataset.pct || '0');
        const offset = circumference - (pct / 100) * circumference;
        ring.style.strokeDasharray = `${circumference}`;
        ring.style.strokeDashoffset = `${offset}`;
    }
});
