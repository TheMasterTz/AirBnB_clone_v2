#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
import os


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class City(BaseModel, Base):
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', backref='cities', cascade='delete')
else:
    class City(BaseModel):
        state_id = ""
        name = ""
