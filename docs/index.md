# Python Backport

## About

_Python Backport_ main goal is to backport functionalities from newer python releases.
It allows using its modules just as the original ones, with the only difference at the import.

Any backported (or experimental) functionality can be imported with the module `py_back`.

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

## Installation

### with pip <small>recommended</small>

_PyBackport_ is published as a [Python package](https://pypi.org/project/PyBackport/) in PyPI and can be installed via pip.

```shell
pip install py-backport
```

### with git

_PyBackport_ can be directly used from [GitHub](https://github.com/Jtachan/PyBackport) by cloning the repository and installing locally. 
```commandline
git clone https://github.com/Jtachan/PyBackport.git
pip install -e py-backport
```

Alternatively, any pip-install-git command can be called over the repository.

```commandline
pip install git+https://github.com/Jtachan/PyBackport.git
```

Latest unreleased changes are also installable by installing the develop branch. Before doing so, consider that they might be breaking changes.

```commandline
pip install git+https://github.com/Jtachan/PyBackport.git@develop
```

---
## Modules index
- **All modules**
    - [enum](enum.md)
    - [colors](colors.md)
- **Backports**
    - [enum](enum.md#backported-classes)
- **Experimental**
    - [enum](enum.md#experimental-classes)