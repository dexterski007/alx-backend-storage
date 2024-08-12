#!/usr/bin/env python3
""" filter topics in python """


def schools_by_topic(mongo_collection, topic):
    """ filter all topics """
    mongo_collection.find({"topic": topic})
