#!/usr/bin/env python3
"""updates documents"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """updates all topics in a collection"""
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
