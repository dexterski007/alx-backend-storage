#!/usr/bin/env python3
""" function to get a page """
import requests
import time
from functools import wraps
from typing import Callable
import redis


redis_client = redis.Redis()


def cacher(url_key: str, expiry: int) -> Callable:
    """ decorator to cache and track number of accesses"""
    def decorator(fn: Callable) -> Callable:
        @wraps(fn)
        def wrapper(url: str) -> str:
            count_key = f"count:{url_key}"
            redis_client.incr(count_key)
            result = redis_client.get(url_key)
            if result:
                return result.decode("utf-8")
            results = fn(url)
            redis_client.setex(url_key, expiry, results)
            return results
        return wrapper
    return decorator


@cacher(url_key='cached', expiry=10)
def get_page(url: str) -> str:
    """ function to get an html page"""
    response = requests.get(url)
    return response.text
