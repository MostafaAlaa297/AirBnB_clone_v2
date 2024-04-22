#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from sqlalchemy.ext.declarative import declarative_base

"""
DBStorage Module
"""

USER = os.getenv('HBNB_MYSQL_USER')
PASSWORD = os.getenv('HBNB_MYSQL_PWD')
HOST = os.getenv('HBNB_MYSQL_HOST')
DATABASE = os.getenv('HBNB_MYSQL_DB')

Base = declarative_base()


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
            USER, PASSWORD, HOST, DATABASE
            ), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        """Return all data"""
        all_classes = [State, City]
        cls_dict = {}
        if cls is None:
            for entry in all_classes:
                for record in self.__session.query(entry).all():
                    #print(record)
                    key = "{}.{}".format(record.__class__.__name__, record.id)
                    cls_dict[key] = record
        else:
            for record in self.__session.query(cls).all():
                print(record)
                key = "{}.{}".format(record.__class__.__name__, record.id)
                cls_dict[key] = record
        return cls_dict

    def new(self, obj):
        """Add a new record"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit changes"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Delete a record"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create session and tables"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """call remove"""
        self.__session.remove()
