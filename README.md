# protonfixes	

A module for applying fixes at runtime to unsupported games with Steam Proton without changing game installation files. The idea is to include seperate fixes that are only loaded when a game matching that ID is run. This should keep the individual game fixes from affecting any other games.

Current fixes include: 
- Final Fantasy IX
- Oddworld: Abe's Oddysee
- Forts

## Installation

### Install from PIP
```
# sudo pip install cecdaemon
```

### Install using setuptools
```
# sudo python setup.py install
```
### Add to user_settings.py
In the steamapps/common/Proton* directory, add the following line to `user_settings.py`:
```
import protonfixes
```
If there is no `user_settings.py` file, make a copy the `user_settings.sample.py` file.

## Writing Game Fixes
Game fixes written in python and are named by the Steam game ID with the extension .py. For example, the file `gamefixes/377840.py` will be loaded when the game FINAL FANTASY IX is run. Here are some things to consider when writing fixes:

- Only import libraries that are part of the Python standard library for portability.
- Use docstrings and comment thoroughly. There will likely be people without python experience making game fixes and good commented examples will help
- Do not use any hard-coded paths, Steam may not always be installed in the same location.
- Check your gamefix with pylint. You can safely disable warning C0103, modules named by Steam ID will never conform to snake_case naming style.
