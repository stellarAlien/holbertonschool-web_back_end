#!/usr/bin/env python3
'''
implement password security
'''

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound

def _hash_password(password: str) -> bytes:
    '''returns salted hash of password'''
    p = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return p

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()
    
    def register_user(self, email=None, password=None) -> User:
        '''register user if not already registered'''
        try:
            user = self._db.find_user_by(email=email)
            if  user:
                raise ValueError('User {:s} already exists'.format(email))
        except NoResultFound:       
            h_p = _hash_password(password)
            user = self._db.add_user(email, h_p)

        return user
        
    def valid_login(self, email, password) -> bool:
        '''validate credentials'''
        if not email or not password:
            return False
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
        
        
        