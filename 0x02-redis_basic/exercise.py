#!/usr/bin/env python3
"""sample python redis implementation module"""
import redis
import uuid


class Cache():
    """redis class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()
    def store(self, data):
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
