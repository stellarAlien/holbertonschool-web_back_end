#!/usr/bin/env python3


from functools import wraps
from typing import Any, Callable, Optional, Union
import redis
import uuid


# count = {}
def call_history(method: Callable) -> Callable:
    @wraps(method)
    def save_io(self, *args, **kwargs):
        """save input and ouput of a method in redis cache"""
        inputs = str(args)
        self._redis.rpush(f'{method.__qualname__}:inputs', inputs)
        outputs = method(self, inputs)
        self._redis.rpush(f'{method.__qualname__}:outputs', outputs)
        return outputs
    return save_io


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """increment counter for calling funciton in redis cache"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

  
class Cache():
    '''cache that is linked to a db'''

    def __init__(self) -> None:
        '''init db'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''store random key in db'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """documentation for get funcion that uses conversion"""
        if not fn:
            value = self._redis.get(key)
        else:
            value = fn(self._redis.get(key))
        return value

    def get_str(self, key):
        '''call get with str function'''
        return self.get(key, str)

    def get_int(self, key):
        '''exec get with int conversion'''
        return self.get(key, int)
