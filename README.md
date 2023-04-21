# CatMap_GIF_Maker

CatMap_GIF_Maker is a Python application that takes a PNG and iterates it through [Arnold's Cat Map](https://en.wikipedia.org/wiki/Arnold%27s_cat_map). Returning a GIF of the animation.

For example take the image given below:

![pythonLogo.png](https://github.com/MatthewWhitaker1/CatMap_GIF_Maker/blob/main/Images/pythonLogo.png?raw=true)

When iterated through Arnold's Cat Map 121 times (since this image has a period of 121):

![pythonLogo.gif](https://github.com/MatthewWhitaker1/CatMap_GIF_Maker/blob/master/GIFs/pythonLogo.gif?raw=true)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install scikit-image as this will install all dependencies needed if not downloaded already.

```bash
pip install scikit-image
```

## Usage

```python
python .\main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
