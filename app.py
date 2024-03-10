from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)
with open("data.txt", 'r') as raw_data:
        data = int(raw_data.read())
def counter():
    with open("data.txt", 'r') as raw_data:
        data = int(raw_data.read())
    data+=1
    with open("data.txt", 'w') as raw_data:
        raw_data.write(str(data))

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/my-link1/')
def my_link1():
    import smtplib

    email = "pjouho@gmail.com"
    receiver_email = "pjouho@gmail.com"

    subject = "Chores-Dishes"
    message = "Your mom has requested you to do the dishes."

    text = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(email, "ajvu kogj ypgp adbf")

    server.sendmail(email, receiver_email, text)

    print("Email has been sent to " + receiver_email)
    counter()
    return redirect(url_for("index"))

@app.route('/my-link2/')
def my_link2():
    import smtplib

    email = os.getenv("EMAIL")
    receiver_email = os.getenv("EMAIL")

    subject = "Chores-Laundry"
    message = "Your mom has requested you to do the laundry."

    text = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(email, "ajvu kogj ypgp adbf")

    server.sendmail(email, receiver_email, text)

    print("Email has been sent to " + receiver_email)
    counter()
    return redirect(url_for("index"))
@app.route('/my-link3/')
def my_link3():
    import smtplib

    email = os.getenv("EMAIL")
    receiver_email = os.getenv("EMAIL")

    subject = "Chores-Trash"
    message = "Your mom has requested you to take out the trash."

    text = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(email, "ajvu kogj ypgp adbf")

    server.sendmail(email, receiver_email, text)

    print("Email has been sent to " + receiver_email)
    counter()
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
