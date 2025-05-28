from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base  # Import Base from models/__init__.py

class Director(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    style = Column(String)

    movies = relationship('Movie', back_populates='director')
