## This project is obsolete.  See https://github.com/imayhaveborkedit/discord-ext-speedups

# discord-ext-copus
Cython bindings of libopus for discord.py

## Installation
`pip install discord-ext-copus`

## Usage
```py
from discord.ext import copus
copus.install()
```
This monkeypatches the extension objects into discord.py, replacing the pure-python+ffi ones.  To revert this simply call `copus.uninstall()`.

## But why?
I know replacing C code interaction with slightly more C code interaction isn't going to net any big gains.  This was made mostly as an experiment for use in future projects.

## Requirements
- Python 3.6.4+
- discord.py

Compiling from source requires:
- cython 0.27.3
