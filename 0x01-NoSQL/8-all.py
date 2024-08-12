#!/usr/bin/env python3
""" list all documents in python """


def list_all(mongo_collection):
    """ list all docs in mongodb """
    return list(mongo_collection.find())
