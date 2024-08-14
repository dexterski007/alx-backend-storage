#!/usr/bin/env python3
""" function to get a page """
import requests
import time
from functools import wraps
from typing import Callable
import redis


redis_client = redis.Redis()


def cacher(expiry: int = 10) -> Callable:
    """ decorator to cache and track number of accesses"""
    def decorator(fn: Callable) -> Callable:
        @wraps(fn)
        def wrapper(url: str) -> str:
            cache_key = "cache:" + url
            cached_content = redis_client.get(cache_key)
            if cached_content:
                return cached_content.decode("utf-8")
            content = fn(url)
            redis_client.setex(cache_key, expiry, content)
            return content
        return wrapper
    return decorator


def counter() -> Callable:
    """ decorator to count functio naccess"""
    def decorator(fn: Callable) -> Callable:
        @wraps(fn)
        def wrapper(url: str) -> str:
            count_key = str("count:" + url)
            redis_client.incr(count_key)
            print (count_key)
            return fn(url)
        return wrapper
    return decorator


@counter()
@cacher(expiry=10)
def get_page(url: str) -> str:
    """ function to get an html page"""
    response = requests.get(url)
    return response.text
