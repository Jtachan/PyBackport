# Unreleased

---

- Defined `CONTRIBUTING.md` and `CHANGELOG.md`

# Release v0.2.0 (March 21, 2024)

---

- Backported from python 3.11:
    - `enum.ReprEnum` to be used for new builtin-type enums.
    - `enum.StrEnum` for enumerations where members are strings.
    - `enum.IntEnum` and `enum.IntFlag` use now `__format__` and `__str__` from the builtins types.
- Defined `enum.TupleEnum` for enumerations where members are tuples.
- Constants defined: `colors.BGR` and `colors.RGB` from `enum.TupleEnum`.
