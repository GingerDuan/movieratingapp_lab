"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db

import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route("/")
def homepage():
    '''go to homepage'''

    return render_template('homepage.html')

@app.route("/movies")
def all_movies():
    """ view all movies """
    movies = crud.all_movies()

    return render_template("all_movies.html", movies=movies)

@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """ Show details on a particular movie. """
    movie = crud.get_movie_by_id(movie_id)

    return render_template("movies_details.html", movie=movie)

@app.route("/users")
def all_users():
    """ view all users """
    users = crud.all_users()

    return render_template("all_users.html", users=users)

@app.route("/users/<user_id>")
def show_user(user_id):
    """ Show details on a particular user. """
    user = crud.get_user_by_id(user_id)

    return render_template("user_detail.html", user=user)


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
