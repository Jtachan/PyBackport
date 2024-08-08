"""Backported enum types."""

import builtins
import enum
import sys
import warnings
from enum import auto

__all__ = ["auto", "IntEnum"]

if sys.version_info >= (3, 11):
    from enum import (
        ReprEnum,
        StrEnum,
    )

    warnings.warn(
        "Using the following classes from the standard library: "
        "StrEnum, EnumCheck, ReprEnum, FlagBoundary, property, member, nonmember, "
        "global_enum, show_flag_values\n"
    )

else:

    class ReprEnum(enum.Enum):
        """Updates 'repr', leaving 'str' and 'format' to the builtin class."""

        def __str__(self):
            return self.value.__str__()

        def __format__(self, format_spec):
            return self.value.__format__(format_spec)

    class IntEnum(ReprEnum, enum.IntEnum):
        """Enum where members are also (and must be) ints."""

    class IntFlag(ReprEnum, enum.IntFlag):
        """Support for integer-based Flags."""

    class StrEnum(builtins.str, ReprEnum):
        """Enum where members are also (and must be) strings."""

        def __new__(cls, *values):
            """Method copied from original enum.StrEnum code.
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
