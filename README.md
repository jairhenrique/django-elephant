# django-elephant

[![Build Status](https://travis-ci.org/jairhenrique/django-elephant.svg)](https://travis-ci.org/jairhenrique/django-elephant)
[![PyPI version](https://badge.fury.io/py/django-elephant.svg)](https://badge.fury.io/py/django-elephant)
[![Coverage Status](https://coveralls.io/repos/jairhenrique/django-elephant/badge.svg?branch=master&service=github)](https://coveralls.io/github/jairhenrique/django-elephant?branch=master)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/03084631935244baa8335617d6502d11/badge.svg)](https://www.quantifiedcode.com/app/project/03084631935244baa8335617d6502d11)


*django-elephant is a simple wrapper to cache responses of Django methods or functions*


## Setup

```bash
pip install django-elephant
```

## Usage

#### Using default cache:

```python
from elephant import memorize

def make_cache_key(function, *args, **kwargs):
    return function.__name__

@memorize(cache_key=make_cache_key, timeout=10000)
def foo(bar):
    return bar
```


#### Using other cache configuration:

```python
from django.core.cache import caches
from elephant import memorize

other_cache = caches['other_cache']

def make_cache_key(function, *args, **kwargs):
    return function.__name__

@memorize(
    cache_key=make_cache_key,
    timeout=10000,
    cache=other_cache
)
def foo(bar):
    return bar
```


## Requirements
- Django>=1.5


## Todo
- Create generic cache key function
