"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb ratings")
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as w:
    movie_data = json.loads(w.read())


movies_in_db = []
for movie in movie_data:
    title, overview, poster_path,release_date = (
        movie["title"],
        movie["overview"],
        movie["poster_path"],
        datetime.strptime(movie['release_date'],"%Y-%m-%d")
    )
    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)

model.db.session.add_all(movies_in_db)
model.db.session.commit()
    

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    db_user = crud.create_user(email,password)
    model.db.session.add(db_user)

    
    for i in range(10):
        random_movie = choice(movies_in_db)
        score = randint(1, 5)

        rating = crud.create_rating(db_user, random_movie, score)
        model.db.session.add(rating)

model.db.session.commit()