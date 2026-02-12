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

from enum import *

if sys.version_info < (3, 11):
    from ._back_enum import IntEnum, IntFlag, ReprEnum, StrEnum

    EnumType = EnumMeta
