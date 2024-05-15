#!/usr/bin/env python3
"""sample python redis implementation module"""
import redis
import uuid
from typing import Callable, Union, Any


class Cache():
    """redis class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable) -> Union[int, str, None, bytes]:
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        return value

    def get_str(self, val: str) -> Union[str, None]:
        return str(val)

    def get_int(self, val: str) -> Union[int, None]:
        return int(val)
