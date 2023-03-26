#!/usr/bin/python3

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, query, scoped_session
from models.base_model import base
from os import getenv, environ
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    "Database engine"

    __engine = None
    __session = None

    def __init__(self):
        """initializes class and engine"""

        user = environ["HBNB_MYSQL_USER"]
        password = environ["HBNB_MYSQL_PWD"]
        host = environ["HBNB_MYSQL_HOST"]
        database = environ["HBNB_MYSQL_DB"]

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                user, password, host,
                database), echo=False, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        "this method must return a dictionary with requested info"
        new_dict = {}
        if cls is None:
            obj = self.__session.query(State).all()
            obj.extend(self.__session.query(User).all())
            obj.extend(self.__session.query(Review).all())
            obj.extend(self.__session.query(Place).all())
            obj.extend(self.__session.query(City).all())
            obj.extend(self.__session.query(Amenity).all())
        else:
            obj = (self.__session.query(cls).all())
        for item in obj:
            new_dict[f"{item.__class__.__name__}.{item.id}"] = item
        return new_dict

    def new(self, obj):
        """add object to current database session"""
        self.__session.add(obj)

    def save(self):
        """saves changes to session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from current database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates session and tables"""
        base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """ Close method to call remove() method """
        self.__session.close()
