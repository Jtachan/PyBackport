"""Test the 'builtins' module."""
from py_back.builtins import str


def test_str_functions():
    my_str = str("Hello world!")
    assert my_str.removesuffix("!") == "Hello world"
