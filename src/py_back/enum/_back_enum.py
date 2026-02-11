"""Backported enum types.

All enumerations can be imported just like the ones provided by python.
```python
from py_back import enum

class Number(enum.IntEnum):
    \"\"\"Enumeration using the original 'IntEnum' call\"\"\"
    ONE = enum.auto()
    TWO = 2


class Animal(enum.StrEnum):
    \"\"\"Supported original 'StrEnum' for python versions < 3.11\"\"\"
    CAT = enum.auto()
    DOG = "dog"
```

Importing the `py_back.enum` module ensures that only the required classes are
backported.
"""

from __future__ import annotations

import enum

from py_back import builtins

# New in Python 3.11
EnumType = enum.EnumMeta


class ReprEnum(enum.Enum):
    """Updates `repr`, leaving `str` and `format` to the builtin class.

    _ReprEnum_ uses the repr() of Enum, but the str() of the mixed-in data type.
    The class is used for any builtin type enum.

    Backported from Python 3.11.
    """

    def __str__(self) -> str:
        """String through the builtin class."""
        return self.value.__str__()

    def __format__(self, format_spec: str) -> str:
        """Format through the builtin class."""
        return self.value.__format__(format_spec)


class IntEnum(ReprEnum, enum.IntEnum):
    """Enum where members are also (and must be) ints.

    `IntEnum` is the same as `Enum`, but its members are also integers and
    can be used anywhere that an integer can be used.

    Backports
    ---------
    Python 3.11:
        Class inherits from `ReprEnum` to leave the `str()` and `format()` to
        the builtin class.

    Notes
    -----
    [`__str__()`](https://docs.python.org/3/reference/datamodel.html#object.__str__)
    is now `int.__str__()` to better support the replacement of existing
    constants use-case.
    [`__format__()`](https://docs.python.org/3/reference/datamodel.html#object.__format__)
    was already `int.__format__()` for that same reason.
    """


class IntFlag(ReprEnum, enum.IntFlag):
    """Support for integer-based Flags.

    IntFlag is the same as Flag, but its members are also integers and can be
    used anywhere that an integer can be used.

    Backports
    ---------
    Python 3.11:
        Class inherits from `ReprEnum` to leave the `str()` and `format()` to
        the builtin class.

    Notes
    -----
    [`__str__()`](https://docs.python.org/3/reference/datamodel.html#object.__str__)
    is now `int.__str__()` to better support the replacement of existing
    constants use-case.
    [`__format__()`](https://docs.python.org/3/reference/datamodel.html#object.__format__)
    was already `int.__format__()` for that same reason.
    """


class StrEnum(builtins.str, ReprEnum):
    """Enum where members are also (and must be) strings.

    `StrEnum` is the same as
    [`Enum`](https://docs.python.org/3.12/library/enum.html#enum.Enum), but
    its members are also strings and can be used in most of the same places
    that a string can be used.

    Examples
    --------
    ```pycon
    >>> from py_back import enum
    >>> class Animal(enum.StrEnum):
    ...    CAT = enum.auto()
    ...    DOG = "dog"
    ...
    >>> Animal.CAT
    cat
    >>> Animal.DOG.title()
    'Dog'
    >>> Animal.CAT == "cat"
    True
    >>> Animal.CAT + Animal.DOG
    'catdog'
    >>> " and ".join(list(Animals))
    'cat and dog'
    ```

    Notes
    -----
    Using [`auto`](https://docs.python.org/3.12/library/enum.html#enum.auto)
    results in the lower-cased member name as the value.
    """

    def __new__(cls, *values) -> StrEnum:
        """Create new StrEnum.

        Method copied from original enum.StrEnum code.
        Values must already be of type `str`.
        """
        if len(values) > 3:
            raise TypeError(f"Too many arguments for str(): {values}")
        if len(values) == 1 and not isinstance(values[0], str):
            # Must be a string.
            raise TypeError(f"{values[0]} is not a string")
        if len(values) >= 2 and not isinstance(values[1], str):
            # check that encoding argument is a string
            raise TypeError(f"Encoding must be a string, not {values[1]}")
        if len(values) == 3 and not isinstance(values[2], str):
            # check that errors argument is a string
            raise TypeError(f"Errors must be a string, not {values[2]}")
        value = str(*values)
        new_member = str.__new__(cls, value)
        new_member._value_ = value
        return new_member

    @staticmethod
    def _generate_next_value_(name: str, *_) -> str:
        """Return the lower-cased version of the member name."""
        return name.lower()
