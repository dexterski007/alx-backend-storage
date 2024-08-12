#!/usr/bin/env python3
""" insert new doc in python """


def insert_school(mongo_collection, **kwargs):
    """ insert new doc in python """
    results = mongo_collection.insert_one(kwargs)
    return results.inserted_id
