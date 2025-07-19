import re
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail, Message
import json
import os
import logging
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from dotenv import load_dotenv


load_dotenv()

# Load non-sensitive parameters from config.json
with open('config.json', 'r') as f:
    params = json.load(f)["params"]

app = Flask(__name__)

# Configure logging for production
if not app.debug:
    logging.basicConfig(level=logging.INFO)

# Configuration
database_uri = os.getenv("DATABASE_URI", "sqlite:///MyPortfolio.db")
# Ensure the instance directory exists for SQLite
if database_uri.startswith('sqlite:///'):
    os.makedirs('instance', exist_ok=True)
    
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin' 

# Define the user class for Flask-Login
class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class dastable(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phonenum = db.Column(db.String(20), nullable=False, unique=True)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    date_submit = db.Column(db.DateTime, default=datetime.now)

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = os.getenv("GMAIL_ID")
app.config['MAIL_PASSWORD'] = os.getenv("GMAIL_PASSWORD")

mail = Mail(app)

def is_valid_email(email): 
    '''Validate email address using regex.'''
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 
    return re.match(email_regex, email)

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == os.getenv("ADMIN_USERNAME") and password == os.getenv("ADMIN_PASSWORD"):
            user = User(id=username)
            login_user(user)
            return redirect(url_for('admindashboard'))
        else:
            return render_template('invalid.html', params=params)
        
    return render_template('admin.html', params=params)

@app.route("/")
def index():
    return render_template("index.html", params=params)

@app.route("/submit_form", methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phonenum = request.form.get('phoneno')
        subject = request.form.get('subject')
        message = request.form.get('message')

        if not is_valid_email(email): 
            flash("Invalid email address.", "error") 
            return redirect(url_for('index'))

        # Validate form data
        if not all([name, email, phonenum, subject, message]):
            flash("All fields are required.", "danger")
            return redirect(url_for('index'))

        try:
            entry = dastable(name=name, email=email, phonenum=phonenum, subject=subject, message=message)
            # Add to the database and commit
            db.session.add(entry)
            db.session.commit()

            # Send confirmation email to the user
            usr_msg = Message(
                "Thank you for reaching out!",
                sender=os.getenv("GMAIL_ID"),
                recipients=[email],
                body=f"""Hello {name},\n\nThank you for reaching out. We have received your message and will get back to you shortly.\n\nYour Message: {message}\n\nBest Regards"""
            )
            mail.send(usr_msg)
            print("EMAIL SENT TO THE USER..")

            # Send email notification to the admin
            admin_msg = Message(
                "New message from " + name,
                sender=os.getenv("GMAIL_ID"),
                recipients=[os.getenv("GMAIL_ID")],
                body=f"""Hello {params['portfolio_name']},\n\nNew message from {name}:\n\n{message}\n\nFrom: {name}\nSubject : {subject}\nEmail: {email}\nPhone Number: {phonenum}"""
            )
            mail.send(admin_msg)
            print("EMAIL SENT TO THE ADMIN..")

            flash("Message sent successfully!", "success")
            return redirect(url_for('index'))

        except Exception as e:
            flash(f"There was an issue adding your entry: {e}", "danger")
            return redirect(url_for('index'))

@app.route("/invalid")
def invalid():
    return render_template("invalid.html", params=params)

@app.route("/admindashboard")
@login_required
def admindashboard():
    try:
        data = dastable.query.all()
        return render_template("admindashboard.html", datas=data, params=params)
    except Exception as e:
        app.logger.error(f"Error in admindashboard: {str(e)}")
        flash("An error occurred while loading the dashboard.", "danger")
        return redirect(url_for('admin'))

@app.route("/delete/<int:srno>", methods=['GET', 'POST'])
@login_required
def delete(srno):
    try:
        record = dastable.query.get(srno)
        if record:
            db.session.delete(record)
            db.session.commit()
            flash("Record deleted successfully!", "success")
        else:
            flash("Record not found.", "danger")
    except Exception as e:
        flash(f"Error occurred while deleting record: {e}", "danger")
    return redirect(url_for('admindashboard'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin'))

@app.route("/udemy")
def udemy():
    return render_template("udemy.html", params=params)

@app.route("/nptel")
def nptel():
    return render_template("nptel.html", params=params)

@app.route("/charusat")
def charusat():
    return render_template("charusat.html", params=params)

@app.route("/other")
def other():
    return render_template("other.html", params=params)

@app.route("/coursera")
def coursera():
    return render_template("coursera.html", params=params)

@app.route("/mongodb")
def mongodb():
    return render_template("mongodb.html", params=params)

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f"Internal Server Error: {str(error)}")
    return render_template("invalid.html", params=params), 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template("invalid.html", params=params), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    # Get port from environment variable for deployment
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
