# -*- coding: utf-8 -*-
import inspect


def _namespace(obj):
    module = obj.__module__ or __name__

    if hasattr(obj, '__qualname__'):
        name = obj.__qualname__
        return '.'.join((module, name))

    klass = getattr(obj, '__self__', None)

    if klass and not inspect.isclass(klass):
        klass = klass.__class__

    if not klass:
        klass = getattr(obj, 'im_class', None)

    if klass:
        name = klass.__name__ + '.' + obj.__name__
    else:
        name = obj.__name__

    return '.'.join((module, name))


def generic(obj, *args, **kwargs):

    _args = None
    _kwargs = None

    generic_key = _namespace(obj)

    if args:
        _args = '.'.join(map(str, args))
        generic_key = generic_key + '.' + _args

    if kwargs:
        _kwargs = '.'.join(
            [
                '_'.join(map(str, data))
                for data in zip(kwargs.keys(), kwargs.values())
            ]
        )

        generic_key = generic_key + '.' + _kwargs

    return generic_key
