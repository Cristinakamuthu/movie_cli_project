from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class Director(declarative_base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    style = Column(String)

    movies = relationship('Movie', back_populates='director')
