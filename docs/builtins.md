# PyBackport: Builtins

`py_back` allows using the `builtins` module just as the original.
However, they must be imported and initialized by converting the instance:

```pycon
# Python version lower than 3.9
>>> from py_back.builtins import str

>>> my_string = str("Hello world!")
>>> print(my_string.removesuffix("!"))
Hello world
```

## str

### [_str_.**removeprefix**(prefix, /)](https://docs.python.org/3/library/stdtypes.html#str.removeprefix)

If the string starts with the prefix string, return string[len(prefix):]. Otherwise, return a copy of the original string:

```pycon
from py_back.builtins import str

>>> str('TestHook').removeprefix('Test')
'Hook'

>>> str('BaseTestCase').removeprefix('Test')
'BaseTestCase'
```

> Backported from python 3.9.

### [_str_.**removesuffix**(suffix, /)](https://docs.python.org/3/library/stdtypes.html#str.removesuffix)

If the string ends with the suffix string and that suffix is not empty, return string[:-len(suffix)]. Otherwise, return a copy of the original string:

```pycon
from py_back.builtins import str

>>> str('MiscTests').removesuffix('Tests')
'Misc'

>>> str('TmpDirMixin').removesuffix('Tests')
'TmpDirMixin'
```

## dict

### [d | other](https://docs.python.org/3/library/stdtypes.html#typesmapping:~:text=values()%0AFalse-,d%20%7C%20other,-Create%20a%20new)

Create a new dictionary with the merged keys and values of d and other, which must both be dictionaries. The values of other take priority when d and other share keys.

> Backported from python 3.9

### [d |= other](https://docs.python.org/3/library/stdtypes.html#typesmapping:~:text=in%20version%203.9.-,d%20%7C%3D%20other,-Update%20the%20dictionary)

Update the dictionary d with keys and values from other, which may be either a [mapping](https://docs.python.org/3/glossary.html#term-mapping) or an [iterable](https://docs.python.org/3/glossary.html#term-iterable) of key/value pairs. The values of other take priority when d and other share keys.

> Backported from python 3.9
