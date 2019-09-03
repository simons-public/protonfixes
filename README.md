# protonfixes	

[![Build Status](https://travis-ci.com/simons-public/protonfixes.svg?branch=master)](https://travis-ci.com/simons-public/protonfixes)

**NOTE: Newer versions of Proton since 4.11-2 have changed how things are accessed. Please use the master branch if you are using an up to date version of Proton. Porting compatibility with older versions is on the todo list.**

![Screenshot](https://github.com/simons-public/protonfixes/raw/master/media/splash.png)

A module for applying fixes at runtime to unsupported games with Steam Proton without changing game installation files. The idea is to include seperate fixes that are only loaded when a game matching that ID is run. This should keep the individual game fixes from affecting any other games. Applying the fixes at runtime should also get them to persist after game updates.

A [list of current fixes](https://github.com/simons-public/protonfixes/wiki/List-of-Fixes), [guide for writing game fixes](https://github.com/simons-public/protonfixes/wiki/Writing-Gamefixes), and details on [game fix utilities](https://github.com/simons-public/protonfixes/wiki/Gamefix-Utilities) can be found on the Wiki. Sources for gamefixes can be found in the [protonfixes/gamefixes](https://github.com/simons-public/protonfixes/tree/master/protonfixes/gamefixes) directory.

---
## Installation

### Optional Requirements
**Winetricks**

If you want to be able to use fixes with winetricks it must be installed and be in your $PATH. Fixes that do not use winetricks will still work without winetricks being installed.

*Winetricks can take a long time to run*

**Wine**

If you want to use a win32 (32bit) prefix, you need to have wine installed and be in your $PATH. Currently creating a 32bit prefix with Proton wine doesn't work because the wineserver is already running by the time `user_settings.py` is loaded.

**Progress Dialog / Splashscreen**

If Steam is in big picture mode, protonfixes will try to launch a similarly themed splash dialog using `cefpython` (pictured above). Otherwise it will try to use `zenity` to display a progress bar. If Steam is not in big picture mode, it will default to `zenity`. The progress bar or splashscreen can help let you know that protonfixes is running a long task, for example installing `dotnet35`.

For the progress dialog to work, you need to have `zenity` installed on your system, the steam-runtime version is broken. It can probably be installed using your distro's package manager.

For the big screen splashscreen to work, you need to have `cefpython3` installed. It can be installed with pip using `sudo pip install cefpython3`.

### Install from PIP
Make sure to use the version of pip that matches the version of Python that Proton is running. Proton should be running on [python3](https://github.com/ValveSoftware/Proton/blob/8a5b8ece45fa7baa01ce2e4555f6496ea409adcf/build_proton.sh#L682). If you are unsure, try installing with both pip3 and pip2 in the below commands.
```
# sudo pip3 install protonfixes
```
To install the latest version from Github:
```
# sudo pip3 install git+https://github.com/simons-public/protonfixes@master
```

### Upgrade from PIP
To upgrade to the latest version on Pypi:
```
# sudo pip3 install protonfixes --upgrade
```
To upgrade to the latest version on Github:
```
# sudo pip3 install --upgrade git+https://github.com/simons-public/protonfixes@master
```

### Install using setuptools
```
# sudo python3 setup.py install
```

### Add to user_settings.py
In the steamapps/common/Proton* directory, add the following line to the bottom of the `user_settings.py` file:
```
import protonfixes
```
If there is no `user_settings.py` file, make a copy of the `user_settings.sample.py` file included with Proton.

---
## Contributing
Pull requests are welcome! If you're not comfortable doing pull requests, send your fixes to me by any other means and you will be credited in the comments.
