from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_year = Column(Integer)
    director_id = Column(Integer, ForeignKey('directors.id'))
    main_actor_id = Column(Integer, ForeignKey('actors.id'))

    director = relationship('Director', back_populates='movies')
    main_actor = relationship('Actor', back_populates='movies')
