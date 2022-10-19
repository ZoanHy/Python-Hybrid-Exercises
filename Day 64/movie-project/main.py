from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import null, desc
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


# -------- Get API --------
URL = "https://api.themoviedb.org/3/"
FIND_MOVIE = "https://api.themoviedb.org/3/movie/?api_key=71aa2f1925317c30fa164225647cf45d"
IMG_MOVIE = "https://image.tmdb.org/t/p/original"
API_KEY = '71aa2f1925317c30fa164225647cf45d'


app = Flask(__name__)
db = SQLAlchemy()

FOLDER = "C:/Users/ASUS/BK University/5_Self_Study/6_PythonHybrid/db"

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{FOLDER}/movies.db'
db.init_app(app)
Bootstrap(app)


class MovieFormEdit(FlaskForm):
    rating = StringField(
        label='Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    done = SubmitField('Done')


class MovieFormFind(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    add = SubmitField('Add Movie')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # db.session.add(new_movie)
    # db.session.commit()
    movies = db.session.query(Movie).order_by(desc('rating')).all()
    for i in range(len(movies)):
        movies[i].ranking = i + 1
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    id_movie = request.args.get('id')
    movie_find = Movie.query.get(id_movie)
    form = MovieFormEdit()
    if form.validate_on_submit():
        movie_find.rating = float(form.rating.data)
        movie_find.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie_find, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_find = Movie.query.get(movie_id)
    db.session.delete(movie_find)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = MovieFormFind()
    if request.method == 'POST':
        query = form.title.data
        query_string_list = {
            'api_key': API_KEY,
            'query': query
        }
        reponse = requests.get(
            url=f"{URL}search/movie/", params=query_string_list)
        list_movie = reponse.json()['results']
        return render_template('select.html', movies=list_movie)
    return render_template('add.html', form=form)


@app.route('/find')
def find():
    id_movie = request.args.get('id')
    query_string_find = {
        'api_key': API_KEY
    }
    reponse = requests.get(
        url=f"{URL}/movie/{id_movie}", params=query_string_find)
    movie_find = reponse.json()
    new_movie = Movie(
        title=movie_find['original_title'],
        year=movie_find['release_date'].split('-')[0],
        description=movie_find['overview'],
        img_url=f"{IMG_MOVIE}/{movie_find['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
