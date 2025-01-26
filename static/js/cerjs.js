const certificates = document.querySelectorAll('.certificate');
const overlay = document.getElementById('overlay');
const certificateViewer = document.getElementById('certificate-viewer');
const closeBtn = document.getElementById('close-btn');
const certificateFrame = document.getElementById('certificate-frame');

certificates.forEach(cert => {
    cert.addEventListener('click', () => {
        const certificateId = cert.id;
        const certificateFilePath = `certificates/${certificateId}.pdf`; // Adjust path and file type
        certificateFrame.src = certificateFilePath;
        overlay.style.display = 'flex';
    });
});

closeBtn.addEventListener('click', () => {
    overlay.style.display = 'none';
    certificateFrame.src = '';
});
