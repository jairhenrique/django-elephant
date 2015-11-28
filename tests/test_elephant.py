# -*- coding: utf-8 -*-
import pytest

from elephant import memorize
from elephant.exceptions import CacheKeyFunctionNotDefined
from django.core.cache import cache as default_cache


class TestElephant(object):

    def test_should_raise_exception_when_cache_key_functions_is_not_defined(self):  # noqa

        @memorize()
        def dumbo():
            return 'dumbo'

        with pytest.raises(CacheKeyFunctionNotDefined):
            assert dumbo() == 'dumbo'

    def test_should_save_result_on_cache(self):

        @memorize(
            timeout=10,
            cache_key=lambda function: 'a'
        )
        def dumbo():
            return 'dumbo'

        assert dumbo() == 'dumbo'

        data = default_cache.get('a')

        assert data == 'dumbo'
