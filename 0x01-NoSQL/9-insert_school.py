#!/usr/bin/env python3
"""inserts a document in a collection"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """inserts a new collection"""
    id_ = mongo_collection.insert_one(kwargs).inserted_id
    return id_
