"""Test the 'enums' module."""
from py_back import enum


def test_repr_enum():
    """
    Testing behaviors in existing enums that were modified in newer python releases,
    due to the creation of ReprEnum.
    The used classes are obtained from the documentation examples.
    """

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


def test_str_enum():
    """Testing py_back.enum.StrEnum"""

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


def test_tuple_enum():
    """Testing py_back.enum.TupleEnum"""

    class Color(enum.TupleEnum):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

    for c in Color:
        assert isinstance(c, tuple), "Type not defined correctly"
        assert c[0] in c, "tuple functions are not working"

    assert list(Color) == [(255, 255, 255), (0, 0, 0)], "Formatting not working"
