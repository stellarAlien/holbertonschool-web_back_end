#!/usr/bin/env python3


from functools import wraps
from typing import Any, Callable, Optional
import redis
import uuid


# count = {}
def call_history(method: Callable) -> Callable:
    @wraps(method)
    def save_io(*args):
        ''''''
        # need to get back to why it worked like this
        for i in args:
            inputs = i
        args[0]._redis.rpush(f'{method.__qualname__}:inputs', str(inputs))
        outputs = method(*args)
        args[0]._redis.rpush(f'{method.__qualname__}:outputs', str(outputs))
        return outputs
    return save_io


def count_calls(fn):
    @wraps(fn)
    def wrapper(*args):
        ''''''
        args[0]._redis.incr(fn.__qualname__)
        return fn(*args)
    return wrapper


class Cache():
    '''cache that is linked to a db'''

    def __init__(self) -> None:
        '''init db'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Any) -> str:
        '''store random key in db'''
        key = str(uuid.uuid4())
        if self._redis.exists(key):
            return
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = str):
        '''get stored value'''
        # if not self._redis.exists(key) :
        # return
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
