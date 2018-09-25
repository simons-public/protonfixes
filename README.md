# protonfixes	

A very basic modular method for applying fixes to run unsupported games with Steam Proton. The idea is to include seperate fixes that are only loaded when a game matching that ID is run. This should keep the individual game fixes from affecting any other games.

## Installation

1. [Download](https://github.com/simons-public/protonfixes/archive/1.0.0.zip) the latest release .zip file and extract it.

2. Move the `protonfixes` folder to the `Proton 3.7` or `Proton 3.7 Beta` directory. 

	This is usually located at `~/.steam/steam/steamapps/common/Proton 3.7` or `~/.local/share/Steam/steamapps/common/Proton 3.7` unless you have Steam installed to another location

3. If you are already using a customized `user_settings.py` file, skip to step 4. Otherwise, copy the `user_settings.py` file into the same Proton directory as the `protonfixes` folder.

4. If you are already using a customized `user_settings.py` and do not want to change your current settings, you can just import the protonfixes module in your `user_settings.py` file by adding the following lines:

		```
		from protonfixes.protonfix import ProtonFix
		ProtonFix()
		```

## Writing Game Fixes
Game fixes written in python and are named by the Steam game ID with the extension .py. For example, the file `gamefixes/377840.py` will be loaded when the game FINAL FANTASY IX is run. Here are some things to consider when writing fixes:

- Only import libraries that are part of the Python standard library for portability.
- Use docstrings and comment thoroughly. There will likely be people without python experience making game fixes and good commented examples will help
- Do not use any hard-coded paths, Steam may not always be installed in the same location.
- Check your gamefix with pylint. You can safely disable warning C0103, modules named by Steam ID will never conform to snake_case naming style.
