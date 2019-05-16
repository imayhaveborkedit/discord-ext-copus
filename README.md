# discord-ext-copus
Cython bindings of libopus for discord.py

## How to install
Run `setup.py build_ext -i` to build the extension.  I will add the install code later.  For now just merge the folders with your discord install in site-packages. (This means just copy the copus folder into discord/ext)

## Requirements
- Python 3.6 or 3.7, might work on 3.5 too
- cython
- discord.py