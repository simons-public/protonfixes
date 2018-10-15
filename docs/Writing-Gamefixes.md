## Writing Game Fixes
Game fixes are written in python and are named by the Steam game ID with the extension .py. For example, the file `377840.py` will be loaded when the game FINAL FANTASY IX is run. Gamefixes can be added to the `~/.config/protonfixes/localfixes/` directory. Here are some things to consider when writing fixes:

- Only import libraries that are part of the Python standard library for portability.
- Use docstrings and comment thoroughly. There will likely be people without python experience making game fixes and good commented examples will help
- Do not use any hard-coded paths, Steam may not always be installed in the same location.
- Check your gamefix with pylint. You can safely disable warning C0103, modules named by Steam ID will never conform to snake_case naming style.

### Testing
When testing, local fixes can be added to `~/.config/protonfixes/localfixes/`. They should be imported the same way as an included fix would be. For example, `~/.config/protonfixes/localfixes/377840.py` would be loaded for FFIX. Please feel free to submit working gamefixes to improve the project. 

### Debugging
Proton output can be seen in either `/tmp/dumps/${USER}_stdout.txt` or the terminal you started Steam from. To add additional `protonfixes` debugging information, add the following line above `import protonfixes`:
```
from protonfixes import debug
```
This will add information like this:
```
ProtonFixes[27351] DEBUG: ---- begin protontricks debug info ----
ProtonFixes[27351] DEBUG: Proton Python Version:
ProtonFixes[27351] DEBUG: /usr/bin/python3
ProtonFixes[27351] DEBUG: 3.7.0 (default, Jul 15 2018, 10:44:58)
[GCC 8.1.1 20180531]
ProtonFixes[27351] DEBUG: ---------------------------------------
```
Although the environment variables are dumped, the sensitive variables like SteamUser and SteamAppUser are filtered out.


### Gamefix utilities 
These helper functions can be used in a game fix by importing the util submodule:
```python
from protonfixes import util
```

- `util.protontricks('verb')`
	-  installs a winetricks verb
- `util.use_win32_prefix()`
	- creates and uses a win32 (32bit) wineprefix
- `util.replace_command('original', 'replacement')`
	- replaces text in the game's launch command
- `util.append_argument('argument')`
	- adds an argument to the game's launch command
- `util.protonprefix()`
	- returns the path of the current wineprefix used by Proton
- `util.set_environment('VARIABLE', 'value')`
	- sets an environment variable
- `util.winedll_override('dllname', 'x')`
	- override dllname where x is n for native, b for builtin, or '' for disable
- winedll_override shortcuts:
	- `util.disable_dxvk()`
	- `util.disable_esync()`
	- `util.disable_d3d10()`
	- `util.disable_d3d11()`
	- `util.disable_nvapi()`
- `util.get_game_install_path()`
	- returns the path to the current game
- `util.create_dosbox_conf('filename', conf_dict)`
	- creates a config file filename with the dict conf_dict
	  _(needs to have '-conf' and 'filename' added with util.append_argument for dosbox use config)_


---
### Example game fixes
`377840.py` - Changing the executable launched and setting an environment variable
```python
""" Game fix for FINAL FANTASY IX
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Changes the proton argument from the launcher to the game
    """

    log('Applying fixes for FINAL FANTASY IX')

    # Fix crackling audio
    util.set_environment('PULSE_LATENCY_MSEC', '60')

    # Replace launcher with game exe in proton arguments
    util.replace_command('FF9_Launcher.exe', 'x64/FF9.exe')
```

`410900.py` - Running a winetricks verb
```python
""" Game fix for Forts
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Uses winetricks to install the ole32 verb
    """

    log('Applying fixes for Forts')

    util.protontricks('ole32')
```
`15700.py` - Example using a win32 prefix

*Oddworld doesn't actually require a win32 prefix or dotnet35, but I used it for testing since it's 32bit*
```python

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Adds -interline to arguments, uses a win32 prefix, and installs dotnet35
    """
    
    log('Applying fixes for Oddworld: Abe\'s Oddysee')
        
    # Adding -interline fixes slow video but adds scanlines
    util.append_argument('-interline')
    
    log('Using a win32 prefix')
    util.use_win32_prefix()
    
    # Make sure any winetricks are run after changing to a win32 prefix
    util.protontricks('dotnet35')
```


