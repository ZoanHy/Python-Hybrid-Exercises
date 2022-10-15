from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align:center;">Hello World!</h1>'\
        '<p>This is a paragraph</p>'\
        '<img width="200" src="https://giphy.com/clips/bestfriends-animals-best-friends-adoption-6PDPcKMAd3CGYXP6a7"></img>'\
        '<div style="width:200px"><iframe allow="fullscreen" frameBorder="0" height="200" src="https://giphy.com/embed/6PDPcKMAd3CGYXP6a7/video"></iframe></div>'


def make_bold(func):
    def wrapper_func():
        text = str(func())
        return f"<b>{text}</b>"
    return wrapper_func


def make_emphasis(func):
    def wrapper_func():
        text = str(func())
        return f"<em>{text}</em>"
    return wrapper_func


def make_underlined(func):
    def wrapper_func():
        text = str(func())
        return f"<u>{text}</u>"
    return wrapper_func


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == '__main__':
    app.run(debug=True)
