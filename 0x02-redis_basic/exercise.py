#!/usr/bin/env python3
"""sample python redis implementation module"""
import redis
import uuid
from typing import Callable, Union, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """wrapper around Cache.store method
    Args:
        method-> function wrapped around this function
    Return:
        the calling method but first sets/increments the number
        of times the function is called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """implements the wrapping functionality
        https://docs.python.org/3.7/library/functools.html#functools.wraps
        """
        key = method.__qualname__
        if self._redis.get(key) is None:
            self._redis.set(key, 1)
        else:
            self._redis.incr(key, 1)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """redis class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, int, float, bytes]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[int, str, None]:
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        return value

    def get_str(self, val: str) -> Union[str, None]:
        return str(val)

    def get_int(self, val: str) -> Union[int, None]:
        return int(val)
