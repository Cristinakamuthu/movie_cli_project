from lib.models import session
from lib.models.movie import Movie
from lib.models.actor import Actor
from lib.models.director import Director

def get_all_movies():
    return session.query(Movie).all()

def get_all_actors():
    return session.query(Actor).all()

def get_all_directors():
    return session.query(Director).all()

def find_movie_by_id(id):
    return session.query(Movie).filter(Movie.id == id).first()

def create_movie(title, year, director_id, actor_id):
    movie = Movie(title=title, release_year=year, director_id=director_id, main_actor_id=actor_id)
    session.add(movie)
    session.commit()
    return movie

def update_movie(id, title=None, year=None, director_id=None, actor_id=None):
    movie = find_movie_by_id(id)
    if movie:
        if title:
            movie.title = title
        if year:
            movie.release_year = year
        if director_id:
            movie.director_id = director_id
        if actor_id:
            movie.main_actor_id = actor_id
        session.commit()
    return movie

def delete_movie(id):
    movie = find_movie_by_id(id)
    if movie:
        session.delete(movie)
        session.commit()
        return True
    return False
