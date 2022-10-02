#!/usr/bin/env python3
"""
password encryptiohn module
"""
from typing import ByteString
import bcrypt
import logging


def hash_password(password: str) -> ByteString:
    '''hash and salt a  password '''
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''check if password provided is the password stored'''
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    return False
