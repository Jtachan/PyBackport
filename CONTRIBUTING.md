# Contributing to PyBackport

The `py_back` module provides access to backported functionalities in new python releases, as well as some experimental ones.
The main goal of providing this access is for the use of these functionalities in packages that must be available for multiple releases.
Consider that not everything can always be backported.

No experimental typings should be added here. If you are looking for that approach, take a look first into [`typing_extensions`](https://github.com/python/typing_extensions).

## Workflow

1. **Address an issue**: Make sure there is an issue before any new PR is open. If no issue exists yet about your new feature or fix, create it.
2. **Open a PR**: You'll need to fork the repository first. When the PR is open, make sure to link the address of the issue within its comment box. Add also the link to the PR within the open issue, so other people can see the issue is already in progress.
3. **Follow the correct guidelines**: To keep the workflow organized:
    - Follow [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html).
    - Use code formatting with [`black`](https://pypi.org/project/black/) and [`isort`](https://pypi.org/project/isort/).
    - Check that [`pylint`](https://pypi.org/project/pylint/) and [`flake8`](https://pypi.org/project/flake8/) don't raise warnings about your code.
4. **Tests**: All new classes should have test under `unittests\test_<module_name>.py` and compatible with [`pytest`](https://pypi.org/project/pytest/).
5. **Changelog**: Update your changes into the changelog, signing your work as following:

```markdown
# Release v1.2.3 (May 15, 2019)

---

- Enumerate your changes

Signed-off-by: Jtachan (jim.gomez.dnn@gmail.com)
```

## Versioning

PyBackport uses [Semantic Versioning](https://semver.org/).
The current content is not enough as for publishing a release v1.
