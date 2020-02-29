""" Game fix for Thief Gold
"""
#pylint: disable=C0103

import os
from protonfixes import util
from protonfixes import download

TFIX_GDRIVE_ID = '1m4Epy8qvHHKjVKp0k0pFYV9HxAmOyKvp'
TFIX_FILENAME = 'TFix_1.27.exe'
TFIX_SHA1SUM = 'd474287ab21c964614c9a972da33f8b03e0a5bd7'
THIEF_EXE_TFIX_SHA1SUM = '80e67c6cc05efa0d5c4f580176fe5cd992371688'


def main():
    """ Need to install vcrun2008 and TFix
    """

    util.protontricks('vcrun2008')
    prefix = util.protonprefix()
    # The TFix silent options only works with C:\Games\Thief
    game_path = util.get_game_install_path()
    games_path = os.path.join(prefix, 'drive_c', 'Games')
    tf_games_path = os.path.join(games_path, 'Thief')
    if not os.path.islink(tf_games_path):
        os.makedirs(games_path, exist_ok=True)
        os.symlink(game_path, tf_games_path)
    tfix_path = os.path.join(game_path, TFIX_FILENAME)
    if not (os.path.isfile(tfix_path)
            and download.sha1sum(tfix_path) == TFIX_SHA1SUM):
        download.gdrive_download(TFIX_GDRIVE_ID, game_path)
    thief_exe = os.path.join(game_path, 'THIEF.EXE')
    if download.sha1sum(thief_exe) != THIEF_EXE_TFIX_SHA1SUM:
        util.wine_run([TFIX_FILENAME, '/S'])
