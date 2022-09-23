#!/usr/bin/env python3
'''
module with least recently used cache
'''
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''Most recently used'''
    def __init__(self) -> None:
        super().__init__()
        self.cache_data = OrderedDict()
    def put(self, key, item):
        '''put wit h mru method'''
        if(not key or not item):
            return
        self.cache_data[key] = item
        if(len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS):
            k = self.cache_data.popitem(last=False)[0]
            print('Discard: {}'.format(k))
            self.cache_data.move_to_end(key, last=False)

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
