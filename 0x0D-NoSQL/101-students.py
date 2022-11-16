#!/usr/bin/env python3
"""returns all students sorted by average score"""


def top_students(mongo_collection):
    '''returns all students sorted by average score'''
    r = mongo_collection.aggregate([
         {"$unwind": "$topics"},
         {"$group":
             {
                 "_id": "$_id",
                 "name": {"$first": '$name'},
                 "averageScore": {"$avg": "$topics.score"}
             }
          },
         {"$sort": {"averageScore": -1}}
     ])
    return r
