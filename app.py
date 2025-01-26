import re
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail, Message
import json
import os

# Load configuration from JSON file
with open('config.json', 'r') as f:
    params = json.load(f)["params"]

app = Flask(__name__)

# Set the SQLite database URI (file-based)
app.config["SQLALCHEMY_DATABASE_URI"] = params['database_uri']

# Set secret key for sessions and flash messages
app.secret_key = os.urandom(24)  # Generate a strong random key

db = SQLAlchemy(app)

# Define the database table model
class dastable(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phonenum = db.Column(db.String(20), nullable=False, unique=True)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    date_submit = db.Column(db.DateTime, default=datetime.now)

# Configure mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = params['gmail_id']
app.config['MAIL_PASSWORD'] = params['gmail_password']

mail = Mail(app)

# Email validation function
def is_valid_email(email): 
    '''Validate email address using regex.'''
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 
    return re.match(email_regex, email)

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == params['admin_username'] and password == params['admin_password']:
            session['user'] = username
            return redirect(url_for('admindashboard'))
        else:
            return render_template('invalid.html')
        
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
                sender=params['gmail_id'],
                recipients=[email],
                body=f"""Hello {name},\n\nThank you for reaching out. We have received your message and will get back to you shortly.\n\nYour Message: {message}\n\nBest Regards"""
            )
            mail.send(usr_msg)
            print("EMAIL SENT TO THE USER..")

            # Send email notification to the admin
            admin_msg = Message(
                "New message from " + name,
                sender=params['gmail_id'],
                recipients=[params['gmail_id']],
                body=f"""Hello {params['portfolio_name']},\n\nNew message from {name}:\n\n{message}\n\nFrom: {name}\nEmail: {email}\nPhone Number: {phonenum}"""
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
def admindashboard():
    data = dastable.query.all()
    return render_template("admindashboard.html", datas=data, params=params)

@app.route("/delete/<int:srno>", methods=['GET', 'POST'])
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


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
