from lib.models import Base, engine, session
from lib.models.movie import Movie
from lib.models.actor import Actor
from lib.models.director import Director

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

actor1 = Actor(name='Cristina Wanjiku', age=24)
actor2 = Actor(name='Michael Mramba', age=30)

director1 = Director(name='Matthew Stanley', style='Action')

movie1 = Movie(title='Rise of the Devs', release_year=2025, director=director1, main_actor=actor1)
movie2 = Movie(title='Codebound', release_year=2025, director=director1, main_actor=actor2)

session.add_all([actor1, actor2, director1, movie1, movie2])
session.commit()
