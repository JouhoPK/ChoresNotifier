from flask import Flask, render_template, redirect, url_for
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/my-link/')
def my_link():
    import smtplib

    email = os.getenv("EMAIL")
    receiver_email = os.getenv("EMAIL")

    subject = "Chores"
    message = "Your mom has requested you to do the dishes."

    text = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(email, "ajvu kogj ypgp adbf")

    server.sendmail(email, receiver_email, text)

    print("Email has been sent to " + receiver_email)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
