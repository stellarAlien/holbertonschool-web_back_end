#!/usr/bin/env python3
'''
implement password security
'''

import bcrypt
from db import DB
from user import User

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
        kwargs = {'email': email}
        user = self._db.find_user_by(**kwargs)
        if not user:
            raise ValueError('User {:s} already exists'.format(email))
            
        h_p = _hash_password(password)
        setattr(user, 'hashed_password', h_p)

        self._db.commit()

        return user
        