from re import A
from turtle import pos
from flask import Flask, render_template
from post import Post
import requests

blog_url = "https://api.npoint.io/7d9bd59bfc5609ea5100"
reponse = requests.get(blog_url)

app = Flask(__name__)

all_posts = reponse.json()
post_array = []
for post in all_posts:
    post_array.append(Post(post['id'], post['title'], post['subtitle']))


@app.route('/')
def home():
    return render_template("index.html", posts=post_array)


@app.route('/post/<id>')
def get_post(id):
    post_find = None
    for post in post_array:
        if str(post.id) == str(id):
            post_find = post
            break
    return render_template('post.html', post=post_find)


if __name__ == "__main__":
    app.run(debug=True)
