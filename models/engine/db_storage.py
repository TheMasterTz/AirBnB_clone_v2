#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage():
    """connection with the database"""
    __engine = None
    __session = None

    def __init__(self):
        """
        __init__ [summary]
        """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                        format(HBNB_MYSQL_USER,
                                                HBNB_MYSQL_PWD,
                                                HBNB_MYSQL_HOST,
                                                HBNB_MYSQL_DB),
                                        pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(Amenity).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(User).all())
        else:
            res_list = res_list = self.__session.query(cls)
        return {'{}.{}'.format(type(obj).__name__, obj.id): obj
                for obj in res_list}


    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def delete(self, obj):
        """Deletes object from storage dictionary"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Reload objects to current db session
        """
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = session_fact()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.close()
