#!/usr/bin/python3
""" A python file that contains the class definition of a City
and an instance Base = declarative_base()
"""
from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """Model class that inherits from Base

    __tablename__: The name of mysql table to store states
    id: The id of state
    name: The state name
    """

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
