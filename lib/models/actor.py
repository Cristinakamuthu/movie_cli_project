from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    movies = relationship('Movie', back_populates='main_actor')
