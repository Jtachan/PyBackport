"""Module to backport 'builtins' classes depending on the system python."""

import sys
import warnings
from builtins import *

__all__ = [name for name in dir() if not name.startswith("_")]

if sys.version_info >= (3, 9):
    warnings.warn(
        "Importing from the standard builtins library: " "dict, str\n",
        stacklevel=2,
    )
else:
    from ._back_builtins import dict, str
