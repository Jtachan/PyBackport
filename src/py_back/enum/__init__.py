"""Module to backport 'enum' classes depending on the system python."""

import sys

__all__ = [
    "Enum",
    "EnumMeta",
    "EnumType",
    "Flag",
    "IntEnum",
    "IntFlag",
    "ReprEnum",
    "StrEnum",
    "auto",
    "unique",
]

if sys.version_info < (3, 11):
    from enum import Enum, EnumMeta, Flag, auto, unique

    from ._back_enum import EnumType, IntEnum, IntFlag, ReprEnum, StrEnum
else:
    from enum import *
