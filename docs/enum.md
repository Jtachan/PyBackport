# PyBackport: Enumerations

`py_back` allows using the `enum` module just as the original, with the only difference at the import.

```python
from py_back import enum


class Number(enum.IntEnum):
    """Enumeration using the original 'IntEnum' call"""
    ONE = enum.auto()
    TWO = 2


class Animal(enum.StrEnum):
    """Supported original 'StrEnum' for python versions < 3.11"""
    CAT = enum.auto()
    DOG = "dog"


class Color(enum.TupleEnum):
    """Experimental 'TupleEnum' class"""
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
```

---
## Backported classes

### [_enum._**IntEnum**](https://docs.python.org/3/library/enum.html#enum.IntEnum)

_IntEnum_ is the same as _Enum_, but its members are also integers and can be used anywhere that an integer can be used.

**Backported from version 3.11**: 
[`__str__()`](https://docs.python.org/3/reference/datamodel.html#object.__str__) is now `int.__str__()` to better support the replacement of existing constants use-case.
[`__format__()`](https://docs.python.org/3/reference/datamodel.html#object.__format__) was already `int.__format__()` for that same reason.

### [_enum._**StrEnum**](https://docs.python.org/3.11/library/enum.html#enum.StrEnum)

**Backported from version 3.11**<br/>
_StrEnum_ is the same as [_Enum_](https://docs.python.org/3.12/library/enum.html#enum.Enum), but its members are also strings and can be used in most of the same places that a string can be used.

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

**Note**: Using [`auto`](https://docs.python.org/3.12/library/enum.html#enum.auto) results in the lower-cased member name as the value.

### [_enum._**IntFlag**](https://docs.python.org/3/library/enum.html#enum.IntFlag)

IntFlag is the same as Flag, but its members are also integers and can be used anywhere that an integer can be used.

**Backported from version 3.11**: 
[`__str__()`](https://docs.python.org/3/reference/datamodel.html#object.__str__) is now `int.__str__()` to better support the replacement of existing constants use-case.
[`__format__()`](https://docs.python.org/3/reference/datamodel.html#object.__format__) was already `int.__format__()` for that same reason.

### [_enum._**ReprEnum**](https://docs.python.org/3/library/enum.html#enum.ReprEnum)

_ReprEnum_ uses the repr() of Enum, but the str() of the mixed-in data type.
The class is used for any builtin type enum.

---
## Experimental classes

### _enum._**TupleEnum**

_TupleEnum_ is the same as [_Enum_](https://docs.python.org/3.12/library/enum.html#enum.Enum), but its members are also tuples and can be used anywhere as tuples can be used.

```pycon
>>> from py_back import enum
>>> class Color(enum.TupleEnum):
...    """Experimental 'TupleEnum' class"""
...    BLACK = (0, 0, 0)
...    WHITE = (255, 255, 255)
...
>>> Color.BLACK
(0, 0, 0)
>>> list(Color.WHITE)
[255, 255, 255]
```

**Note**: Using [`auto`](https://docs.python.org/3.12/library/enum.html#enum.auto) is not supported by _TupleEnum_, and it will raise a `NotImplementedError`.
