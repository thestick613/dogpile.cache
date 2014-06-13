from dogpile.cache.backends.null import NullLock
from unittest import TestCase
from _fixtures import _GenericBackendFixture
from dogpile.cache.api import NO_VALUE
from . import eq_
import itertools

class NullBackendTest(_GenericBackendFixture, TestCase):
    backend = "dogpile.cache.null"

    def test_get(self):
        reg = self._region()

        eq_(reg.get("some key"), NO_VALUE)

    def test_set(self):
        reg = self._region()
        reg.set("some key", "some value")
        eq_(reg.get("some key"), NO_VALUE)

    def test_delete(self):
        reg = self._region()
        reg.delete("some key")
        eq_(reg.get("some key"), NO_VALUE)

    def test_get_multi(self):
        reg = self._region()

        eq_(
            reg.get_multi(['a', 'b', 'c']),
            [NO_VALUE, NO_VALUE, NO_VALUE]
        )

    def test_set_multi(self):
        reg = self._region()
        reg.set_multi(
            {
                "a": 1,
                "b": 2,
                "c": 3
            }
        )
        eq_(
            reg.get_multi(['a', 'b', 'c']),
            [NO_VALUE, NO_VALUE, NO_VALUE]
        )

    def test_delete_multi(self):
        reg = self._region()
        reg.delete_multi(["a", "b", "c"])
        eq_(
            reg.get_multi(['a', 'b', 'c']),
            [NO_VALUE, NO_VALUE, NO_VALUE]
        )

    def test_decorator(self):
        reg = self._region()

        counter = itertools.count(1)
        @reg.cache_on_arguments()
        def go(a, b):
            val = next(counter)
            return val, a, b

        eq_(go(1, 2), (1, 1, 2))
        eq_(go(1, 2), (2, 1, 2))
        eq_(go(1, 3), (3, 1, 3))
