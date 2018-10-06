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
If there is no `user_settings.py` file, make a copy of the `user_settings.sample.py` file.

## Writing Game Fixes
Game fixes written in python and are named by the Steam game ID with the extension .py. For example, the file `gamefixes/377840.py` will be loaded when the game FINAL FANTASY IX is run. Here are some things to consider when writing fixes:

- Only import libraries that are part of the Python standard library for portability.
- Use docstrings and comment thoroughly. There will likely be people without python experience making game fixes and good commented examples will help
- Do not use any hard-coded paths, Steam may not always be installed in the same location.
- Check your gamefix with pylint. You can safely disable warning C0103, modules named by Steam ID will never conform to snake_case naming style.
- Pull requests are welcome!

## Example game fixes
`377840.py` - Changing the executable launched
```
import os
import sys


def main():
    """ Changes the proton argument from the launcher to the game
    """

    print('Applying FINAL FANTASY IX Game Fixes')

    # Fix crackling audio
    os.environ['PULSE_LATENCY_MSEC'] = '60'

    # Replace launcher with game exe in proton arguments
    for idx, env in enumerate(sys.argv):
        if 'FF9_Launcher' in env:
            sys.argv[idx] = env.replace('FF9_Launcher.exe', 'x64/FF9.exe')
```

`410900.py` - Running a winetricks verb
```
from protonfixes import util

def main():
    """ Uses winetricks to install the ole32 verb
    """

    print('Applying fixes for Forts')

    if not util.checkinstalled('ole32'):
        util.protontricks('ole32')
```
