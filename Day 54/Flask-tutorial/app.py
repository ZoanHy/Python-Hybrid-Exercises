from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', content="Huy haha!")


@app.route('/admin')
def hello_admin():
    return f"<h1> Hello admin ne shibaaa</h1>"


@app.route('/user/<name>')
def hello_user(name):
    if name == "admin":
        return redirect(url_for('hello_admin'))
    return f"<h1> Hello {name} </h1>"


@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    return f"<h1> Blog {blog_id} </h1>"


if __name__ == '__main__':
    app.run(debug=True)
