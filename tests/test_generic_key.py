# -*- coding: utf-8 -*-
from elephant.keys import generic


def fake(*args, **kwargs):
    pass


class FakeClass(object):

    def fake(self, *args, **kwargs):
        pass


class TestGenericKey(object):

    def test_generic_key_should_return_module_and_function_name(self):
        key = 'tests.test_generic_key.fake'
        assert key == generic(fake)

    def test_generic_key_should_return_module_function_name_and_parameters(self):  # noqa
        args = (10, 20)
        kwargs = {'a': 10, 'b': 20}

        key = 'tests.test_generic_key.fake.10.20'
        assert key == generic(fake, *args)

        key = 'tests.test_generic_key.fake.10.20.a_10.b_20'  # noqa
        assert key == generic(fake, *args, **kwargs)

    def test_generic_key_should_return_module_class_and_method_name(self):
        key = 'tests.test_generic_key.FakeClass.fake'

        fake = FakeClass()
        assert key == generic(fake.fake)

    def test_generic_key_should_return_module_class_methdo_name_and_parameters(self):  # noqa
        args = (10, 20)
        kwargs = {'a': 10, 'b': 20}

        fake = FakeClass()

        key = 'tests.test_generic_key.FakeClass.fake.10.20'
        assert key == generic(fake.fake, *args)

        key = 'tests.test_generic_key.FakeClass.fake.10.20.a_10.b_20'  # noqa
        assert key == generic(fake.fake, *args, **kwargs)
