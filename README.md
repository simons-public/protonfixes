# protonfixes	

## This repository is no longer being maintained. Please direct any future game fixes to the repository maintained by [@GloriousEggroll](https://github.com/GloriousEggroll) at https://github.com/Open-Wine-Components/umu-protonfixes. This allows fixes to be distributed along with ProtonGE which is well-maintained and significantly more useful than protonfixes alone. 

![Screenshot](https://github.com/simons-public/protonfixes/raw/master/media/splash.png)

A module for applying fixes at runtime to unsupported games with Steam Proton without changing game installation files.
The idea is to include separate fixes that are only loaded when a game matching that ID is run.
This should keep the individual game fixes from affecting any other games. Applying the fixes at runtime should also get them to persist after game updates.

A [list of current fixes](https://github.com/simons-public/protonfixes/wiki/List-of-Fixes),
[guide for writing game fixes](https://github.com/simons-public/protonfixes/wiki/Writing-Gamefixes),
and details on [game fix utilities](https://github.com/simons-public/protonfixes/wiki/Gamefix-Utilities) can be found on the [Wiki](https://github.com/simons-public/protonfixes/wiki).
Sources for gamefixes can be found in the [protonfixes/gamefixes](https://github.com/simons-public/protonfixes/tree/master/protonfixes/gamefixes) directory.

---
## Installation

### Optional Requirements
**Winetricks**

If you want to be able to use fixes with winetricks it must be installed and be in your $PATH. Fixes that do not use winetricks will still work without winetricks being installed.

*Winetricks can take a long time to run*

**Wine**

If you want to use a win32 (32bit) prefix, you need to have wine installed and be in your $PATH.
Currently creating a 32bit prefix with Proton wine doesn't work because the wineserver is already running by the time `user_settings.py` is loaded.

**Progress Dialog / Splashscreen**

If Steam is in big picture mode, protonfixes will try to launch a similarly themed splash dialog using `kivy` (pictured above).
`zenity` or `kdialog` can also be used but need to be enabled manually via config.
If Steam is not in big picture mode, it will try `kdialog`, then `zenity`.  
The progress bar or splashscreen can help let you know that protonfixes is running a long task, for example installing `dotnet35`.

For the progress dialog to work, you need to have `zenity` or `kdialog` installed on your system, the steam-runtime version of zenity is broken.  
It can probably be installed using your distro's package manager.

For the big screen splashscreen to work, you need to have `kivy` installed.
It can be installed via your distro's package manager (`python3-kivy` on debian-based distros and `python-kivy` on Arch-based ones)

### Install With PIP
Make sure to use the version of pip that matches the version of Python that Proton is running. Proton should be running on [python3](https://github.com/ValveSoftware/Proton/blob/8a5b8ece45fa7baa01ce2e4555f6496ea409adcf/build_proton.sh#L682). Use `pip` to install from the GitHub repository, the PyPI package is not being maintained at the moment.

If `pip3` is not installed, it can be installed with your distribution's package manager: the package is `python3-pip` on Ubuntu/Debian-based distributions, `python-pip` in many others.

To install the latest version from Github:
```
#  pip3 install git+https://github.com/simons-public/protonfixes
```

### Upgrade from PIP
To upgrade to the latest version on Github:
```
# pip3 install --upgrade git+https://github.com/simons-public/protonfixes
```

### Install using setuptools
```
# python3 setup.py install
```

### Enabling protonfixes in Proton
Protonfixes includes a script `install_protonfixes` that, when run, will automatically install protonfixes in all Proton installations.  
A manual installation is possible by browsing `<Steam installation>/steamapps/common/Proton*` and adding this line to `user_settings.py`

```
import protonfixes
```

If there is no `user_settings.py` file, make a copy of the `user_settings.sample.py` file included with Proton.

---
## Contributing
Pull requests are welcome! If you're not comfortable doing pull requests, send your fixes to me by any other means and you will be credited in the comments.
