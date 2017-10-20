# django-elephant

[![Build Status](https://travis-ci.org/jairhenrique/django-elephant.svg)](https://travis-ci.org/jairhenrique/django-elephant)
[![PyPI version](https://badge.fury.io/py/django-elephant.svg)](https://badge.fury.io/py/django-elephant)
[![codecov.io](https://codecov.io/github/jairhenrique/django-elephant/coverage.svg?branch=master)](https://codecov.io/github/jairhenrique/django-elephant?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a6977c4884fa4c358b699f2d86fc0f50)](https://www.codacy.com/app/jairhenrique/django-elephant?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jairhenrique/django-elephant&amp;utm_campaign=Badge_Grade)


*django-elephant is a simple wrapper to cache responses of Django methods or functions*


## Setup

```bash
pip install django-elephant
```

## Usage

#### Basic:

```python
from elephant import memorize

@memorize()
def foo(bar):
    return bar
```


#### Set cache configuration:

```python
from django.core.cache import caches
from elephant import memorize

other_cache = caches['other_cache']

@memorize(
    cache=other_cache
)
def foo(bar):
    return bar
```


#### Set cache timeout:

```python
from elephant import memorize

@memorize(
    timeout=1987
)
def foo(bar):
    return bar
```

#### Set cache key:

```python
from elephant import memorize

def my_custom_key(function, *args, **kwargs):
    return '{}.{}'.format(
        'elephant_'
        function.__name__
    )

@memorize(
    cache_key=my_custom_key
)
def foo(bar):
    return bar
```

## Requirements
- Django>=1.5


## Contribute
- Fork and make a pull request!
