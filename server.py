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
    # if not "user_email" in session:
    #     return redirect("/login")


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

@app.route("/users", methods= ['POST'])
def register_user():
    """ create new user """

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("This user is already register, try another email")
    else:
        new_user = crud.create_user(email, password)

        db.session.add(new_user)
        db.session.commit()
        flash("Account created! Please log in your account..")

    return redirect("/")

@app.route("/login",methods = ['POST'])
def log_in():
    """ log in to a user account"""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user.password == password:
        session["user_email"] = user.email
        flash(f"Welcome back!!!{user.email}")
    else:
        flash("email or password is not corret, try again!")
    
    return redirect("/")


@app.route("/users/<user_id>")
def show_user(user_id):
    """ Show details on a particular user. """
    user = crud.get_user_by_id(user_id)

    return render_template("user_detail.html", user=user)

@app.route("/movies/<movie_id>/rating",methods=['POST'])
def rating(movie_id):
    """a user rate a movie"""

    score = request.form.get("rating")
    email = session.get["user_email"]

    if email is None:
        flash("You must log in to rate this movie")
    elif score is None:
        flash("Please slecet a score of this movie")
    else:
        user = crud.get_user_by_email(email)
        movie = crud.get_movie_by_id(movie_id)
        rating = crud.create_rating(user, movie, int(score))

        db.session.add(rating)
        db.session.commit()

        flash("rate successfully!!")

    return redirect("/")
        

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
