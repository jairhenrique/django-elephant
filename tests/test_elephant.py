# -*- coding: utf-8 -*-
import pytest

from elephant import memorize
from elephant.exceptions import CacheKeyFunctionNotDefined
from django.core.cache import cache as default_cache


class TestElephant(object):

    def test_should_raise_exception_when_cache_key_functions_is_not_callable(self):  # noqa

        @memorize(cache_key=None)
        def dumbo():
            return 'dumbo'

        with pytest.raises(CacheKeyFunctionNotDefined):
            assert dumbo() == 'dumbo'

    def test_should_use_generic_cache_key(self):
        @memorize()
        def dumbo():
            return 'dumbo'

        assert dumbo() == 'dumbo'

        data = default_cache.get('tests.test_elephant.dumbo')
        assert data == 'dumbo'

    def test_should_save_result_on_cache(self):

        @memorize(
            timeout=10,
            cache_key=lambda function: 'fake_key'
        )
        def dumbo():
            return 'dumbo'

        assert dumbo() == 'dumbo'

        data = default_cache.get('fake_key')

        assert data == 'dumbo'
