"""Backported builtins functionalities."""

from __future__ import annotations

import builtins

__all__ = ["dict", "str"]


class dict(builtins.dict):
    """Backport for 'dict' class.

    <ul>
        <li><code>dict()</code> -> new empty dictionary.</li>
        <li><code>dict(mapping)</code> -> new dictionary initialized from a mapping
            object's (key, value) pairs.</li>
        <li><code>dict(iterable)</code> -> new dictionary initialized as if.</li>
        <li><code>dict(**kwargs)</code> -> new dictionary initialized with the
            <code>name=value</code> pairs in the keyword argument list. E.G.:
            <code>dict(one=1, two=2)</code></li>
    </ul>

    Backports
    ---------
    **Python 3.9**:
        Operators [`d | other`](https://docs.python.org/3/library/stdtypes.html#typesmapping:~:text=values()%0AFalse-,d%20%7C%20other,-Create%20a%20new)
        and [`d |= other`](https://docs.python.org/3/library/stdtypes.html#typesmapping:~:text=in%20version%203.9.-,d%20%7C%3D%20other,-Update%20the%20dictionary).
    """

    def __or__(self, other: builtins.dict) -> dict:
        """Return `self | other`, which is equivalent to `self.update(other)`.

        Create a new dictionary with the merged keys and values of `d` and `other`,
        which must both be dictionaries. The values of `other` take priority when `d`
        and `other` share keys.

        The operation `other | d` is also supported.

        Notes
        -----
        The dictionary defined as `other` does not need to be a backported instance.

        Examples
        --------
        ```pycon
        >>> from py_back.builtins import dict
        >>> dict({"key_0": 1}) | {"key_1": 2}
        {"key_0": 1, "key_1": 2}
        ```
        """
        d = self.copy()
        d.update(other)
        return d

    def __ror__(self, other: builtins.dict) -> dict:
        return self | other


class str(builtins.str):
    """Backport for `str` class.

    <ul>
        <li><code>str(object='')</code> -> <code>str</code></li>
        <li><code>str(bytes_or_buffer[, encoding[, errors]])</code> ->
            <code>str</code></li>
    </ul>

    Backports
    ---------
    **Python 3.9**:
        Methods `str.removeprefix(prefix, /)` and `str.removesuffix(suffix, /)`
    """

    def removeprefix(self, prefix: str) -> str:
        """Backport logic to remove prefix from str.

        If the string starts with the prefix string, return `string[len(prefix):]`.
        Otherwise, return a copy of the original string.

        Examples
        --------
        ```pycon
        from py_back.builtins import str
        >>> str('TestHook').removeprefix('Test')
        'Hook'
        >>> str('BaseTestCase').removeprefix('Test')
        'BaseTestCase'
        ```
        """
        if prefix == self[: len(prefix)]:
            return self[len(prefix) :]
        return self

    def removesuffix(self, suffix: str) -> str:
        """Backport logic to remove suffix from str.

        If the string ends with the suffix string and that suffix is not empty,
        return `string[:-len(suffix)]`. Otherwise, return a copy of the original string.

        Examples
        --------
        ```pycon
        from py_back.builtins import str
        >>> str('MiscTests').removesuffix('Tests')
        'Misc'
        >>> str('TmpDirMixin').removesuffix('Tests')
        'TmpDirMixin'
        ```
        """
        if suffix == self[-len(suffix) :]:
            return self[: -len(suffix)]
        return self
