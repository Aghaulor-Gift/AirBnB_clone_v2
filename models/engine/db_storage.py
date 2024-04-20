#!/usr/bin/python3
"""
Create new engine
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """A class that represent the database storage"""
    __engine=None
    __session=None

    __init__(self):
        """ Initialisation of attributes"""
        self.__engine = created_engine('mysql+mysqldb://{}:{}@{}{}'.format(
                       os.getenv("HBNB_MYSQL_USER"),
                       os.getenv("HBNB_MYSQL_PWD"),
                       os.getenv("HBNB_MYSQL_HOST"),
                       os.getenv("HBNB_MYSQL_DB")),
                       pool_pre_ping=True)
        if (os.getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)

    all(self, cls=None):
        """ A method with the class"""
        session = self.__session
        if cls:
            objs = session.query(cls).all()
        else:
            objs = []
            for c in classes.values():
                objs += session.query(c).all()
        return {type(obj).__name__ + "." + obj.id: obj for obj in objs}

    new(self, obj):
        """Add a new object to the current database session"""
        if obj:
            self.__session.add(obj)

    save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    delete(self, obj=None):
        """Delete the obj of the current database session"""
         if obj:
             self.__session.delete(obj)

    reload(self):
        """Create all tables in the database and create a new session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
