import sys
from pymemcache.client import base


class MemcacheLocal():

    def __init__(self):
        self.local = '127.0.0.1'
        self.port = 11211
        self.cache = None
        try:
            self.cache = base.Client((self.local, self.port))
        except Exception as err:
            print(err)

    def get(self, key):
        res = {}
        try:
            res = self.cache.get(key)
        except Exception as err:
            print(err)
        return res

    def set(self, key, val, exp=7200):
        try:
            res = self.cache.set(key, val, expire=exp)
        except Exception as err:
            print(err)

    def delete_key(self, key):
        try:
            res = self.cache.delete(key)
        except Exception as err:
            print(err)