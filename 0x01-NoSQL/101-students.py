#!/usr/bin/env python3
""" return sorted students in python """


def top_students(mongo_collection):
    """ return sorted students in python """
    pipeline = [
        {
            "$addFields": {
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
        ]
    return list(mongo_collection.aggregate(pipeline))
