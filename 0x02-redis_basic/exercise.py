#!/usr/bin/env python3
""" redis cache setup """
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """ cache class yeah """
    def __init__(self):
        """ instantiation """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn:
            Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ decoder of byte strings """
        data = self._redis.get(key)
        if fn is not None:
            data = fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ str decoder """
        data = self.get(key, fn=lambda a: a.decode('utf-8'))
        return str(data)

    def get_int(self, key: str) -> int:
        """ int decoder """
        data = self.get(key, fn=lambda b: b.decode('utf-8'))
        return int(data)
