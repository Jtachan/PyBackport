# PyBackport: Builtins

`py_back` allows using the `builtins` module just as the original.
However, they must be imported and initialized:

```python
# Python version lower than 3.9
from py_back.builtins import str

my_string: str = "Hello world!"
```
