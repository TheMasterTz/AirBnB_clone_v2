#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv


HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == "db":
    from models.engine.db_storage import DBStorage
    Storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    Storage = FileStorage()

Storage.reload()
