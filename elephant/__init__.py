# -*- coding: utf-8 -*-
import functools

from django.core.cache import cache as default_cache

try:
    from django.core.cache.backends.base import DEFAULT_TIMEOUT
except ImportError:  # Django < 1.6 compatibility
    DEFAULT_TIMEOUT = 300


from elephant.exceptions import CacheKeyFunctionNotDefined


class Elephant(object):
    """
    Elephant
    """
    def __init__(self):
        pass

    def memorize(
        self,
        cache=default_cache,
        cache_key=None,
        timeout=DEFAULT_TIMEOUT
    ):
        def memorize(f):
            @functools.wraps(f)
            def decorated_function(*args, **kwargs):
                if not callable(cache_key):
                    raise CacheKeyFunctionNotDefined()

                key = cache_key(f, *args, **kwargs)

                value = cache.get(key)

                if not value:
                    value = f(*args, **kwargs)
                    cache.set(key, value, timeout)

                return value

            return decorated_function
        return memorize


dumbo = Elephant()
memorize = dumbo.memorize
