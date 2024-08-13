#!/usr/bin/env python3
""" redis cache setup """
import redis
import uuid
from typing import Union


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
