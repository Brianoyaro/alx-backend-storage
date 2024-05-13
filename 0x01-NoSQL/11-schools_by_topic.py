#!/usr/bin/env python3
""" list of school having a specific topic"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ list of school having a specific topic"""
    return mongo_collection.find({"topics": topic})
