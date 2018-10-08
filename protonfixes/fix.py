""" Gets the game id and applies a fix if found
"""

from __future__ import print_function
import os
import re
import sys
from importlib import import_module
try:
    from protonfixes.splash import splash
except ModuleNotFoundError:
    print('No splash, cefpython3 module not available')

def game_id():
    """ Trys to return the game id from environment variables
    """

    if 'SteamAppId' in os.environ:
        return os.environ['SteamAppId']
    if 'SteamGameId' in os.environ:
        return os.environ['SteamGameId']
    if 'STEAM_COMPAT_DATA_PATH' in os.environ:
        return re.findall(r'\d+', os.environ['STEAM_COMPAT_DATA_PATH'])[-1]

    print('Game ID not found in environment variables')
    return None


def run_fix(gameid):
    """ Loads a gamefix module by it's gameid
    """

    if gameid is not None:
        localpath = os.path.expanduser('~/.config/protonfixes/localfixes')
        if os.path.isfile(os.path.join(localpath, gameid + '.py')):
            open(os.path.join(localpath, '__init__.py'), 'a').close()
            sys.path.append(os.path.expanduser('~/.config/protonfixes'))
            try:
                game_module = import_module('localfixes.' + gameid)
                print('Using local protonfix for gameid', gameid)
                game_module.main()
            except ImportError:
                print('No local protonfix found for gameid', gameid)
        else:
            try:
                game_module = import_module('protonfixes.gamefixes.' + gameid)
                print('Using protonfix for gameid', gameid)
                game_module.main()
            except ImportError:
                print('No protonfix found for gameid', gameid)


print('\n\nRunning protonfixes')

if 'cefpython3' in sys.modules:
    with splash():
        run_fix(game_id())
else:
    run_fix(game_id())
