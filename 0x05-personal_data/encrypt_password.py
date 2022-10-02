#!/usr/bin/env python3
"""
password encryptiohn module
"""
from typing import ByteString
import bcrypt
import logging
 
def hash_password(password: str) -> ByteString:
     '''hash and salt a  password '''
     password = password.encode()
     try:
         hashed = bcrypt.hashpw(password, bcrypt.gensalt())
         return hashed
     except  ImportError:
         logging.error('could not import bcrypt')
