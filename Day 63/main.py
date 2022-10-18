from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

# ---------- Create Database -------------

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250),  nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()
    db.session.commit()

all_books = []


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    books = all_books
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        index = len(all_books)
        new_book = Book(
            title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        with app.app_context():
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        id_book = request.form['id']
        book_find = Book.query.get(id_book)
        book_find.rating = float(request.form['rating'])
        db.session.commit()
        return redirect(url_for('home'))

    id_book = request.args.get('id')
    book_find = Book.query.get(id_book)
    return render_template('edit_rating.html', book=book_find)


@app.route('/delete')
def delete():
    id_book = request.args.get('id')
    book_delete = Book.query.get(id_book)
    db.session.delete(book_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
