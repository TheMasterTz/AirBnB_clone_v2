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


class DBStorage:
    """Interaction to DBStorage"""
    __engine__ = None
    __session = None

    def __init__(self,):
        """initialization method"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        var_env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, db),
                                      pool_pre_ping=True)
        if var_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Reurns a dictionary of models currently in storage"""

        if cls is None:
            obj = self.__session.query(User).all()
            obj.extend(self.__session.query(City).all())
            obj.extend(self.__session.query(Amenity).all())
            obj.extend(self.__session.query(Place).all())
            obj.extend(self.__session.query(Review).all())
            obj.extend(self.__session.query(State).all())
        else:
            res_list = res_list = self.__session.query(cls)
        return {'{}.{}'.format(type(obj).__name__, obj.id): obj
                for obj in res_list}

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def new(self, obj):
        """Adds new objects to storage dictionary"""
        self.__session.add(obj)

    def delete(self, obj=None):
        """Deletes object from storage dictionary"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload object to current db session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """Remove session"""
        self.__session.close()
