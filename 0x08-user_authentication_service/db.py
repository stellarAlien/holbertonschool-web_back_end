#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from sqlalchemy.orm.session import Session
from user import User

from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
    
    def add_user(self, email=None, hashed_password=None) -> User:
        '''add user with no validation'''
        if not email or not hashed_password:
            return
        user = User(email = email, hashed_password= hashed_password)
        self._session.add(user)
        self._session.commit()
        # self._session.refresh()
   
        return user
    
    def find_user_by(self, **kwargs):
        '''find user by'''
        # one() raises sqlalchemy.orm.exc.NoResultFound
        # exception if no result is found or many are found
        if not kwargs:
            raise InvalidRequestError
        for key in kwargs.keys():
            if  not key in User.__table__.columns.keys():
                raise InvalidRequestError
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            # one() cause error becasue it required a row
            return user
        except (NoResultFound, InvalidRequestError) as e:
            raise e
    
    def update_user(self, user_id=None, **kwargs) -> None:
        '''update user row'''

        user = self.find_user_by(id= user_id)
        for arg in kwargs.keys():
            if not arg in user.__table__.columns.keys():
                raise ValueError

        for k,v in kwargs.items():    
            setattr(user, k, v)

        self._session.commit()