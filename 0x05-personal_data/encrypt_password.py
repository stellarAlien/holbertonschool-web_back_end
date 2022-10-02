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


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''check if password provided is the password stored'''
    password = password.encode('utf-8')
    if bcrypt.checkpw(password, hashed_password):
        return True
    return False
