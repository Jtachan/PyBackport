# Contributing to PyBackport

The `py_back` module provides access to backported functionalities in new python releases, as well as some experimental ones.
The main goal of providing this access is for the use of these functionalities in packages that must be available for multiple releases.
Consider that not everything can always be backported.

No experimental typings should be added here. If you are looking for that approach, take a look first into [`typing_extensions`](https://github.com/python/typing_extensions).

## Versioning

PyBackport uses [Semantic Versioning](https://semver.org/).
The 'main' branch is defined as `X.Y.Z`, while 'develop' is defined as `X.Y.Z.N`.
The "N" number refers to the pre-release 

The current content is not enough as for publishing a release v1.

## Guidelines

- **Issues and PRs**: Every new addition must be linked to an open issue. Issues and PRs can be linked by their comment boxes.
- **New PRs**: All pull request should be branched and merged into 'develop' for security. New releases will be published into 'main' periodically (if new stable changes exist).
- **Style**: Code in this repository should follow [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html).
- **Linters & formatters**: Keep all code in the correct format using `black`, `isort`, `pylint` and `flake8`. 
- **Tests**: New additions require new test, defined at the _unittests_ folder. 
    - Every module must define the tests as `test_<module_name>.py`.
    - Classes must be tested within their module tests.
    - All tests have to be compatible with `pytest`.
- **Documentation**: Any new code must be documented for the final mkdocs page.
- **Version**: When a PR is accepted, update the package version from `X.Y.Z.N` to `X.Y.Z.N+1`.
- **Changelog**: Include your changes within `CHANGELOG.md`, where newer changes come first.
