#!/usr/bin/python3
""" New engine: DBStorage  """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ This class manages a MySQL Database """
    __engine = None
    __session = None

    def __init__(self):
        """ Create the engine """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        """
        cls_dict = {}  # class dictionary

        if cls is None:
            query = self.__session.query(User, State, City, Amenity,
                                         Place, Review)
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                cls_dict[key] = obj
            return cls_dict  # return dictionary of all class objects
        else:
            query = self.__session.query(cls)
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                cls_dict[key] = obj
            return cls_dict  # return dictionary of all class objects

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        * Create all tables in the database
        * Create the current database session
        """
        # create all tables
        Base.metadata.create_all(self.__engine)
        # create current database session and make sure Session is thread-safe
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """ method to close session on the private session attribute """
        self.__session.close()
