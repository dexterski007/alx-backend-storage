#!/usr/bin/env python3
""" list all documents in python """


def list_all(mongo_collection):
    """ list all docs in mongodb """
    if mongo_collection is None:
        return []
    return [mongo_collection.find()]
