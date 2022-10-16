from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()
MAIL = os.getenv('MAIL')
PASS = os.getenv('PASS')

posts = requests.get("https://api.npoint.io/7d9bd59bfc5609ea5100").json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        new_message = f"Name: {name}\nEmail: {mail}\nPhone: {phone}\nMessage: {message}"
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(MAIL, PASS)
            connection.sendmail(from_addr=mail,
                                to_addrs="huyleezoan@gmail.com",
                                msg=(f"{new_message}").encode("utf-8"))
        return render_template('contact.html', message=True)
    return render_template("contact.html", message=False)


if __name__ == "__main__":
    app.run(debug=True)
