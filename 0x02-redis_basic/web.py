#!/usr/bin/env python3
""" redis cache implement """
import requests
import redis

rcache = redis.Redis()


def get_page(url: str) -> str:
    """ getting html and content """
    rcache.incr(f"count:{url}")
    cache = rcache.get(url)
    if cache:
        return cache.decode('utf-8')
    content = requests.get(url).text
    rcache.setex(url, 10, content)
    return content
