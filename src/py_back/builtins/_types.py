"""Backported builtins functionalities"""
from __future__ import annotations
import builtins


class dict(builtins.dict):
    """
    dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)

    Backports
    ---------
    Py 3.9
        d | other
        d |= other
    """
    def __or__(self, other: builtins.dict):
        d = self.copy()
        d.update(other)
        return d


class str(builtins.str):
    """
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Backports
    ---------
    Py 3.9
        str.removeprefix(prefix, /)
    """
    def removeprefix(self, prefix) -> str:
        """
        If the string starts with the prefix string, return string[len(prefix):].
        Otherwise, return a copy of the original string:
        """
        if prefix == self[:len(prefix)]:
            return self[len(prefix):]
        return self

    def removesuffix(self, suffix) -> str:
        """
        If the string ends with the suffix string and that suffix is not empty,
        return string[:-len(suffix)]. Otherwise, return a copy of the original string.
        """
        if suffix == self[-len(suffix):]:
            return self[:-len(suffix)]
        return self
