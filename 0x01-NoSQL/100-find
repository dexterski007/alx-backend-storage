#!/usr/bin/env python3
""" nginx stats """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    counter = collection.count_documents({})
    print("{} logs".format(counter))
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        counter2 = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {counter2}")
    countpath = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{countpath} status check")
