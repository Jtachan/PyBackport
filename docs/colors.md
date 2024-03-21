# PyBackport: Colors

`py_back.colors` allows easy import and use color codes, commonly used in computer vision applications.

The following are the supported classes:
* _RGB_: Contains red-green-blue color codes as tuples of three ints.
* _BGR_: Contains blue-green-red color codes as tuples of three ints.

**Note**: Due to the existing of many color variations, the supported classes only contain the most common color codes.
All color codes have been extracted from https://www.rapidtables.com/web/color/RGB_Color.html.

```pycon
>>> from py_back import colors
>>> colors.RGB.RED
(255, 0, 0)
>>> colors.BGR.RED
(0, 0, 255)
>>> [c.name for c, _ in zip(colors.RGB, range(5))]
['BLACK', 'WHITE', 'RED', 'GREEN', 'BLUE']
>>> [c for c, _ in zip(colors.RGB, range(5))]
[(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
```

---
### _colors._**RGB**

Each member contains RGB color codes.

- `AQUA`: (0, 255, 255)
- `BLACK`: (0, 0, 0) 
- `BLUE`: (0, 0, 255)
- `CYAN`: (0, 255, 255)
- `DARK_GREEN`: (0, 128, 0)
- `FUCHSIA`: (255, 0, 255)
- `GRAY`: (128, 128, 128)
- `GREEN`: (0, 255, 0)
- `MAGENTA`: (255, 0, 255)
- `MAROON`: (128, 0, 0)
- `NAVY`: (0, 0, 128)
- `OLIVE`: (128, 128, 0)
- `PURPLE`: (128, 0, 128)
- `RED`: (255, 0, 0)
- `SILVER`: (192, 192, 192)
- `TEAL`: (0, 128, 128)
- `WHITE`: (255, 255, 255)
- `YELLOW`: (255, 255, 0)

### _colors._**BGR**

Each member contains BGR color codes.

- `AQUA`: (255, 255, 0)
- `BLACK`: (0, 0, 0) 
- `BLUE`: (255, 0, 0)
- `CYAN`: (255, 255, 0)
- `DARK_GREEN`: (0, 128, 0)
- `FUCHSIA`: (255, 0, 255)
- `GRAY`: (128, 128, 128)
- `GREEN`: (0, 255, 0)
- `MAGENTA`: (255, 0, 255)
- `MAROON`: (0, 0, 128)
- `NAVY`: (128, 0, 0)
- `OLIVE`: (0, 128, 128)
- `PURPLE`: (128, 0, 128)
- `RED`: (0, 0, 255)
- `SILVER`: (192, 192, 192)
- `TEAL`: (128, 128, 0)
- `WHITE`: (255, 255, 255)
- `YELLOW`: (0, 255, 255)
