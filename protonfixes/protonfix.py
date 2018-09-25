""" Loads gamefixes from the gamefixes dir based on game id
"""

from __future__ import print_function
import os
import re
from importlib import import_module

class ProtonFix():
    """ Loads the specific fix for a game from gamefixes
    """

    #pylint: disable=R0903

    def __init__(self):
        self._get_game_id()
        self._import_fix()

    def _import_fix(self):
        try:
            game_module = import_module(re.sub(r'\..*', '.gamefixes.', __name__) + str(self.game_id))
            game_module.main()
            print('Using protonfix for gameid', self.game_id)
        except ImportError:
            print('No protonfix for gameid', self.game_id, 'found')

    def _get_game_id(self):
        """ Try to get the game id from environment variables
        """

        game_id = None
        if game_id is None and 'SteamAppId' in os.environ:
            game_id = int(os.environ["SteamAppId"])
        if game_id is None and 'SteamGameId' in os.environ:
            game_id = int(os.environ["SteamGameId"])
        if game_id is None and 'STEAM_COMPAT_DATA_PATH' in os.environ:
            game_id = int(re.findall(r'\d+', os.environ['STEAM_COMPAT_DATA_PATH'])[-1])

        print('Steam gameid', game_id, 'retrieved from environment variables')
        assert isinstance(game_id, int)
        self.game_id = game_id
