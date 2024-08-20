"""Test the 'enums' module."""
import sys

import pytest


@pytest.mark.skipif(
    sys.version_info >= (3, 11), reason="ReprEnum is available from python 3.11"
)
def test_repr_enum():
    """Tests for enum representations.

    Testing behaviors in existing enums that were modified in newer python releases,
    due to the creation of ReprEnum. The used classes are obtained from the
    documentation examples.
    """
    from py_back import enum

    class Color(enum.IntFlag):
        RED = enum.auto()
        GREEN = enum.auto()

    assert Color.RED & 2 is Color(0)
    assert repr(Color.RED | 2) in ("<Color.RED|GREEN: 3>", "<Color.GREEN|RED: 3>")
    assert str(Color.RED) == "1"

    class Number(enum.IntEnum):
        ONE = 1
        TWO = enum.auto()
        THREE = 3

    assert Number.TWO == 2
    assert Number.ONE + Number.THREE == 4
    assert repr(Number.ONE) == "<Number.ONE: 1>"
    assert str(Number.TWO) == "2"


@pytest.mark.skipif(
    sys.version_info >= (3, 11), reason="StrEnum is available from python 3.11"
)
def test_str_enum():
    """Testing py_back.enum.StrEnum."""
    from py_back import enum

    class Animal(enum.StrEnum):
        DOG = enum.auto()
        CAT = "cat"
        PLATYPUS = enum.auto()

    for pet in Animal:
        assert isinstance(pet, str), "Type not defined correctly"
        assert pet.upper() == str(pet).upper(), "str builtin functions are not working"

    assert list(Animal) == [
        "dog",
        "cat",
        "platypus",
    ], "Formatting not working"
