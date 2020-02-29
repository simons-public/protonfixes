""" Game fix for Thief 2
"""
#pylint: disable=C0103

import os
from protonfixes import util
from protonfixes import download

TFIX_GDRIVE_ID = '13alujC8_7M2NDiLHlBUXsG2EWihGYnVb'
TFIX_FILENAME = 'T2Fix_1.27b.exe'
TFIX_SHA1SUM = '0294bd7a0d8a0888c6820ebe04fec8a3e6fbeb91'
THIEF_EXE_TFIX_SHA1SUM = '8f7cae836380225548d16f568d53db6a76a07735'


def main():
    """ Need to install vcrun2008 and T2Fix
    """

    util.protontricks('vcrun2008')
    prefix = util.protonprefix()
    # The TFix silent options only works with C:\Games\Thief
    game_path = util.get_game_install_path()
    games_path = os.path.join(prefix, 'drive_c', 'Games')
    tf_games_path = os.path.join(games_path, 'Thief 2 The Metal Age')
    if not os.path.islink(tf_games_path):
        os.makedirs(games_path, exist_ok=True)
        os.symlink(game_path, tf_games_path)
    tfix_path = os.path.join(game_path, TFIX_FILENAME)
    if not (os.path.isfile(tfix_path)
            and download.sha1sum(tfix_path) == TFIX_SHA1SUM):
        download.gdrive_download(TFIX_GDRIVE_ID, game_path)
    thief_exe = os.path.join(game_path, 'Thief2.exe')
    if download.sha1sum(thief_exe) != THIEF_EXE_TFIX_SHA1SUM:
        util.wine_run([TFIX_FILENAME, ])
