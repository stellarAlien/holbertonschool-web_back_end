#!/usr/bin/env python3
"""
password encryptiohn module
"""
from typing import ByteString
import bcrypt
import logging


def hash_password(password: str) -> ByteString:
    '''hash and salt a  password '''
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed
    
