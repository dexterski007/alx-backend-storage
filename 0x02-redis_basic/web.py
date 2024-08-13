#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""
import requests
import redis
from functools import wraps

mem = redis.Redis()


def count_url_access(method):
    """Counting how many times a URL is accessed using decorator"""
    @wraps(method)
    def wrapper(url):
        count_key = "count:" + url
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)

        if cached_data:
            return cached_data.decode("utf-8")

        html = method(url)

        mem.incr(count_key)
        mem.set(cached_key, html)
        mem.expire(cached_key, 10)
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """Returns HTML content of a URL"""
    res = requests.get(url)
    return res.text
