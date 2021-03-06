"""CRUD operations."""

from re import U
from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)
    
    return user



def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(
        title=title,
        overview=overview,
        release_date=release_date,
        poster_path=poster_path,)

    return movie

def all_movies():
    '''call all the movies'''

    return Movie.query.all()

def create_rating(user, movie, score):
    """Create and return new rating. """

    rating = Rating(user=user, movie=movie, score=score)

    return rating

def get_movie_by_id(movie_id):
    """found a movie by the movie id"""

    return Movie.query.get(movie_id)


def all_users():
    """Returns all user"""

    return User.query.all()
     
def get_user_by_id(user_id):
    """found a user by the user id"""
    
    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email"""

    return User.query.filter(User.email == email).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)