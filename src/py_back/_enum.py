"""Backported enum types."""
from __future__ import annotations

import builtins
import enum
import sys
import warnings
from enum import Enum, EnumMeta, Flag, auto, unique

__all__ = [
    "auto",
    "IntEnum",
    "ReprEnum",
    "IntFlag",
    "EnumMeta",
    "Enum",
    "EnumType",
    "unique",
    "Flag",
]

if sys.version_info >= (3, 11):
    from enum import EnumType, IntEnum, IntFlag, ReprEnum, StrEnum

    warnings.warn(
        "Using the following classes from the standard library: "
        "IntEnum, IntFlag, ReprEnum, StrEnum, EnumType\n",
        stacklevel=2,
    )

else:
    EnumType = EnumMeta

    class ReprEnum(enum.Enum):
        """Updates 'repr', leaving 'str' and 'format' to the builtin class."""

        def __str__(self) -> str:
            """String through the builtin class."""
            return self.value.__str__()

        def __format__(self, format_spec: str) -> str:
            """Format through the builtin class."""
            return self.value.__format__(format_spec)

    class IntEnum(ReprEnum, enum.IntEnum):
        """Enum where members are also (and must be) ints.
        Backported from py3.11 leaving the str & format to the builtin class.
        """

    class IntFlag(ReprEnum, enum.IntFlag):
        """Support for integer-based Flags.
        Backported from py3.11 leaving the str & format to the builtin class.
        """

    class StrEnum(builtins.str, ReprEnum):
        """Enum where members are also (and must be) strings. Backported from py3.11."""

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
