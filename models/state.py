#!/usr/bin/python3
""" State Module for HBNB project """
"""This is the state class"""
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

if getenv('HBNB_TYPE_STORAGE') == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
else:
    class State(BaseModel):
        name = ""

        @property
        def cities(self):
            """ return the list of City objects from storage linked to
            the current State"""
            city_list = []
            for key, obj in models.storage.all(City).items():
                if obj.state_id == self.id:
                    city_list.append(obj)
            return city_list
