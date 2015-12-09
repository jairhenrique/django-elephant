# -*- coding: utf-8 -*-
from collections import OrderedDict
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
        name = '{}.{}'.format(
            klass.__name__,
            obj.__name__
        )
    else:
        name = obj.__name__

    return '.'.join((module, name))


def generic(obj, *args, **kwargs):

    _args = None
    _kwargs = None

    generic_key = _namespace(obj)

    if args:
        _args = '.'.join(map(str, args))
        generic_key = '{}.{}'.format(
            generic_key,
            _args
        )

    if kwargs:
        kwargs = OrderedDict(sorted(kwargs.items(), key=lambda t: t[0]))

        _kwargs = '.'.join(
            ['_'.join(map(str, item)) for item in kwargs.items()]
        )

        generic_key = '{}.{}'.format(
            generic_key,
            _kwargs
        )

    return generic_key
