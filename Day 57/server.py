import json
from urllib import response
from flask import Flask, render_template
import random
import requests
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, current_year=datetime.today().year, name="Zoan Hy")


@app.route("/guess/<name>")
def guess_name(name):
    gender = requests.get(
        f'https://api.genderize.io/?name={name}').json()['gender']
    print(gender)
    age = requests.get(f'https://api.agify.io/?name={name}').json()['age']
    return render_template('guess.html', name=name.title(), gender=gender, age=age)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/7d9bd59bfc5609ea5100"
    reponse = requests.get(blog_url)
    all_posts = reponse.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
