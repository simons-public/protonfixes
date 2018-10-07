# protonfixes	

A module for applying fixes at runtime to unsupported games with Steam Proton without changing game installation files. The idea is to include seperate fixes that are only loaded when a game matching that ID is run. This should keep the individual game fixes from affecting any other games. Applying the fixes at runtime should also allow fixes to persist after game updates.

Current fixes include: 
- Final Fantasy IX
- Oddworld: Abe's Oddysee
- Forts

## Installation

### Requirements
If you want to be able to use fixes with winetricks it must be installed and be in your $PATH. Fixes that do not use winetricks will still work without winetricks being installed.

*Winetricks can take a long time to load*

If you want to use a win32 (32bit) prefix, you need to have wine installed and be in your $PATH. Currently creating a 32bit prefix with Proton wine doesn't work because wineserver is already running by the time `user_settings.py` is loaded.

### Install from PIP
```
# sudo pip install protonfixes
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

### Testing
When testing, local fixes can be added to `~/.config/protonfixes/localfixes/`. They should be imported the same way as an included fix would be. For example, `~/.config/protonfixes/localfixes/377840.py` would be loaded for FFIX. Please feel free to submit working gamefixes to improve the project. 

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
`15700.py` - Example using a win32 prefix

*Oddworld doesn't actually require a win32 prefix or dotnet35, but I used it for testing since it's 32bit*
```
import sys
from protonfixes import util

def main():
    """ Adds -interline to arguments, uses a win32 prefix, and installs dotnet35
    """
    
    print('Applying fixes for Oddworld: Abe\'s Oddysee')
    
    # Adding -interline fixes slow video but adds scanlines
    sys.argv.append('-interline')
    
    print('Using a win32 prefix')
    util.use_win32_prefix()
    
    # Make sure any winetricks are run after changing to a win32 prefix
    if not util.checkinstalled('dotnet35')
        util.protontricks('dotnet35')
```

## Contributing
Pull requests are welcome! If you're not comfortable doing pull requests, send your fixes to me by any other means and you will be credited in the comments.
