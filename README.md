# 🌟 Kaustav Das - Portfolio Website

A dynamic and responsive portfolio website built with Flask, showcasing my journey as a Computer Engineering student and developer.

## 🚀 Live Demo

Visit the live website: [kaustav-portfolio.onrender.com/](https://kaustav-portfolio.onrender.com/)

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Screenshots](#screenshots)
- [Contact](#contact)
- [License](#license)

## 🎯 About

This portfolio website represents my academic and professional journey as a BTech Computer Engineering student at Charotar University of Science and Technology (CHARUSAT), Gujarat. The site features my projects, certifications, academic achievements, and provides a platform for visitors to connect with me.

### Key Highlights:
- 🎓 BTech in Computer Engineering from CHARUSAT
- 💻 Focus on MERN Stack, Flask, and Python programming
- 📊 Strong foundation in Data Structures and Algorithms
- 🏆 Multiple certifications from Coursera, NPTEL, Udemy, and more

## ✨ Features

### 🏠 Main Features
- **Responsive Design**: Mobile-first approach with Bootstrap framework
- **Dynamic Contact Form**: Integrated email system for visitor inquiries
- **Admin Dashboard**: Secure admin panel for managing contact submissions
- **Certificate Gallery**: Organized display of academic and professional certifications
- **Project Showcase**: Detailed portfolio section highlighting key projects
- **Social Media Integration**: Direct links to LinkedIn, GitHub, Instagram, and Twitter

### 🔐 Security Features
- **Environment Variables**: Sensitive data stored securely
- **Flask-Login**: Authentication system for admin access
- **Email Validation**: Server-side email validation for contact forms
- **Database Security**: SQLite database with proper access controls

### 📧 Email System
- **Automatic Confirmations**: Users receive confirmation emails
- **Admin Notifications**: Real-time email alerts for new submissions
- **Gmail Integration**: Secure SMTP configuration

## 🛠️ Tech Stack

### Backend
- **Framework**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Email**: Flask-Mail with Gmail SMTP
- **Environment**: python-dotenv for configuration

### Frontend
- **Styling**: Bootstrap 4, Custom CSS
- **JavaScript**: jQuery, Custom JS
- **Icons**: Font Awesome, Flaticon
- **Animations**: CSS animations and transitions
- **Responsive**: Mobile-first design approach

### Deployment
- **Platform**: Railway
- **Process**: Gunicorn WSGI server
- **Environment**: Production-ready configuration

## 🚀 Installation

### Prerequisites
- Python 3.8+
- Git
- Gmail account (for email functionality)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/kaustav3071/MyPortfolio.git
   cd MyPortfolio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   
   Create a `.env` file in the root directory:
   ```env
   DATABASE_URI=sqlite:///MyPortfolio.db
   GMAIL_ID=your_email@gmail.com
   GMAIL_PASSWORD=your_app_password
   ADMIN_USERNAME=your_admin_username
   ADMIN_PASSWORD=your_admin_password
   PORTFOLIO_NAME=Your Name
   ```

5. **Initialize Database**
   ```bash
   python app.py
   ```

6. **Run the application**
   ```bash
   flask run
   ```

   Visit `http://localhost:5000` to view the website.

## 📖 Usage

### For Visitors
1. **Explore Portfolio**: Browse through projects, certifications, and achievements
2. **Contact Form**: Use the contact section to send messages
3. **Download Resume**: Access and download the latest resume
4. **Social Links**: Connect through various social media platforms

### For Admin
1. **Access Admin Panel**: Navigate to `/admin` and login with credentials
2. **View Messages**: Check all contact form submissions in the dashboard
3. **Manage Data**: Delete processed messages and manage inquiries
4. **Email Management**: Automatic email notifications for new submissions

## 📁 Project Structure

```
MyPortfolio/
├── app.py                 # Main Flask application
├── config.json           # Configuration parameters
├── requirements.txt       # Python dependencies
├── Procfile              # Railway deployment configuration
├── .env                  # Environment variables (not in repo)
├── .gitignore           # Git ignore rules
├── instance/            # Database storage
│   └── MyPortfolio.db   # SQLite database (not in repo)
├── static/              # Static assets
│   ├── css/            # Stylesheets
│   ├── js/             # JavaScript files
│   ├── images/         # Image assets
│   ├── fonts/          # Web fonts
│   ├── certificate/    # Certificate PDFs
│   ├── certificate page/ # Certificate images
│   ├── download/       # Downloadable files
│   └── logo/           # Logo assets
└── templates/           # HTML templates
    ├── index.html      # Main page
    ├── admin.html      # Admin login
    ├── admindashboard.html # Admin dashboard
    ├── coursera.html   # Coursera certificates
    ├── nptel.html      # NPTEL certificates
    ├── udemy.html      # Udemy certificates
    ├── charusat.html   # University certificates
    ├── mongodb.html    # MongoDB certificates
    ├── other.html      # Other certificates
    └── invalid.html    # Error page
```

## ⚙️ Configuration

### config.json
Main configuration file containing:
- Personal information (name, email, social links)
- Website URLs and external links
- About me content and academic details

### Environment Variables
Secure configuration stored in `.env`:
- Database connection string
- Email credentials (Gmail SMTP)
- Admin authentication credentials

## 🌐 Deployment

### Railway Deployment

1. **Connect Repository**: Link your GitHub repository to Railway
2. **Environment Variables**: Set all required environment variables in Railway dashboard
3. **Database**: Railway automatically handles SQLite database creation
4. **Custom Domain**: Configure custom domain if needed

### Configuration Files
- `Procfile`: Specifies the web server command
- `requirements.txt`: Lists all Python dependencies
- `runtime.txt`: Specifies Python version (if needed)

## 📸 Screenshots

*Add screenshots of your portfolio website here*

## 🎓 Certifications Showcase

The portfolio features organized certificate galleries for:
- **Coursera**: Programming and data science courses
- **NPTEL**: Academic engineering courses
- **Udemy**: Practical skill development
- **CHARUSAT**: University academic achievements
- **MongoDB**: Database certification
- **GitHub**: Development platform certifications
- **Other**: Additional professional certifications

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Contact

**Kaustav Das**
- 📧 Email: kaustavdas2027@gmail.com
- 💼 LinkedIn: [kaustavdas1703](https://www.linkedin.com/in/kaustavdas1703/)
- 💻 GitHub: [kaustav3071](https://github.com/kaustav3071)
- 📷 Instagram: [kaustavdas17](https://www.instagram.com/kaustavdas17/)
- 🐦 Twitter: [kaustav1703](https://x.com/kaustav1703)
- 🔗 LeetCode: [kaustavdas17](https://leetcode.com/u/kaustavdas17/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to CHARUSAT for the academic foundation
- Coursera, NPTEL, and Udemy for excellent online courses
- Open source community for amazing tools and libraries
- Railway for reliable hosting platform

---

⭐ **If you found this project helpful, please give it a star on GitHub!** ⭐

*Last updated: July 2025*
