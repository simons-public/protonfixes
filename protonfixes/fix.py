""" Gets the game id and applies a fix if found
"""

from __future__ import print_function
import os
import re
import sys
from importlib import import_module
from protonfixes.splash import splash
from .logger import log

def game_id():
    """ Trys to return the game id from environment variables
    """

    if 'SteamAppId' in os.environ:
        return os.environ['SteamAppId']
    if 'SteamGameId' in os.environ:
        return os.environ['SteamGameId']
    if 'STEAM_COMPAT_DATA_PATH' in os.environ:
        return re.findall(r'\d+', os.environ['STEAM_COMPAT_DATA_PATH'])[-1]

    log.crit('Game ID not found in environment variables')
    return None


def game_name():
    """ Trys to return the game name from environment variables
    """

    game_library = re.findall(r'.*/steamapps', os.environ['PWD'], re.IGNORECASE)[-1]
    game_manifest = os.path.join(game_library, 'appmanifest_' + game_id() + '.acf')
    try:
        with open(game_manifest, 'r') as appmanifest:
            for x in appmanifest.readlines():
                if 'name' in x.strip():
                    name = re.findall(r'"[^"]+"', x)[-1]
                    return name
    except OSError:
        return 'UNKNOWN'
    return 'UNKNOWN'


def run_fix(gameid):
    """ Loads a gamefix module by it's gameid
    """

    if gameid is not None:
        game = game_name() + ' ('+ gameid + ')'
        localpath = os.path.expanduser('~/.config/protonfixes/localfixes')
        if os.path.isfile(os.path.join(localpath, gameid + '.py')):
            open(os.path.join(localpath, '__init__.py'), 'a').close()
            sys.path.append(os.path.expanduser('~/.config/protonfixes'))
            try:
                game_module = import_module('localfixes.' + gameid)
                log.info('Using local protonfix for ' + game)
                game_module.main()
            except ImportError:
                log.info('No local protonfix found for ' + game)
        else:
            try:
                game_module = import_module('protonfixes.gamefixes.' + gameid)
                log.info('Using protonfix for ' + game)
                game_module.main()
            except ImportError:
                log.info('No protonfix found for ' + game)


def main():
    """ Runs the gamefix, with splash if zenity or cefpython3 is available
    """

    if 'iscriptevaluator.exe' in sys.argv[2]:
        log.debug('Not running protonfixes for iscriptevaluator.exe')
        return

    if 'getcompatpath' in sys.argv[1]:
        log.debug('Not running protonfixes for getcompatpath')
        return

    if 'getnativepath' in sys.argv[1]:
        log.debug('Not running protonfixes for getnativepath')
        return

    log.info('Running protonfixes')
    with splash():
        run_fix(game_id())
