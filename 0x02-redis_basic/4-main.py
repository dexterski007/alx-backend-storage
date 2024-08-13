#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache
replay = __import__('exercise').replay

cache = Cache()

if __name__ == "__main__":

    # Perform some actions
    cache.store("foo")
    cache.store("bar")
    cache.store(42)

    # Replay the history of calls to cache.store
    replay(cache.store)
