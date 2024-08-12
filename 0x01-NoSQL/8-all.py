#!/usr/bin/env python3
""" list all documents in python """


def list_all(mongo_collection):
    """ list all docs in mongodb """
    if mongo_collection is None:
        return []
    new_list = []
    for doc in mongo_collection.find():
        new_list.append(doc)
    return new_list
