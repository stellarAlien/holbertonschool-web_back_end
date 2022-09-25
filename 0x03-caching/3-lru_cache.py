#!/usr/bin/env python3
'''
module with least recently used cache
'''
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''LRU method'''

    def __init__(self) -> None:
        '''init method takes no arguments'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, value):
        '''put method of LRU strategy'''
        if(not key or not value):
            return
        self.cache_data[key] = value
        if(len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS):
            k = self.cache_data.popitem(last=False)[0]
            print('DISCARD: {}'.format(k))
            self.cache_data.move_to_end(key)

    def get(self, key):
        '''get method WITH OrderedDict MECHANIC'''
        if (not key):
            return
        try:
            r = self.cache_data.get(key)
            self.cache_data.move_to_end(key)
            return r
        except Exception:
            return
