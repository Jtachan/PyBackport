"""Module to backport 'builtins' classes depending on the system python.

`py_back` allows using the `builtins` module just as the original.

```pycon
# Python version lower than 3.9
>>> from py_back.builtins import str
>>> my_string = str("Hello world!")
>>> print(my_string.removesuffix("!"))
Hello world
```

!!! Note
    Python builtins don't require to be imported, but the backported builtins do not
    follow this rule. This results in the inconvenience that backported instances must
    be defined with the constructor provided by `py_back`, even if they interact with
    other not backported builtins.
"""

import sys
from builtins import *

__all__ = ["str", "dict"] + list({name for name in dir() if not name.startswith("_")})

if sys.version_info < (3, 9):
    from ._back_builtins import dict, str
