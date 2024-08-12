#!/usr/bin/env python3
""" nginx stats """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    counter = collection.count_documents()
    print("{} logs".format(counter))
    print("Methods:")
    print("")
