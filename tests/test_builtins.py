"""Test the 'builtins' module."""


def test_backported_str():
    """Here are tested all methods backported for the 'str' class."""
    from py_back.builtins import str

    old_str = "Hello world!"

    for backported_method in ("removeprefix", "removesuffix"):
        assert hasattr(old_str, backported_method) is False

    assert str("TestHook").removeprefix("Test") == "Hook"
    assert str("BaseTestCase").removeprefix("Test") == "BaseTestCase"

    assert str("MiscTests").removesuffix("Tests") == "Misc"
    assert str("TmpDirMixin").removesuffix("Tests") == "TmpDirMixin"


def test_backported_dict():
    """Here are tested all methods backported for the 'str' class."""
    from py_back.builtins import dict

    my_dict = dict({"a": 1, "b": 2})
    result = my_dict | {"c": 3}
    assert my_dict == {"a": 1, "b": 2}
    assert result == {"a": 1, "b": 2, "c": 3}
