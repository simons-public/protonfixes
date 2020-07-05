""" Game fix for Spaceport Hope
"""
#pylint: disable=C0103

import os
import shutil
from protonfixes import util

def main():
    """ Add OpenAL dll to java, replace launcher """
    copy_openal()
    util.replace_command('EQLauncher.exe', 'space.exe')


@util.once
def copy_openal():
    """ Copy OpenAL*.dll to the java dir to avoid the audio
        being sent to the wrong audio card
    """
    gamedir = util.get_game_install_path()
    shutil.copy(os.path.join(gamedir, 'OpenAL32.dll'),
                os.path.join(gamedir, 'jre/bin'))
    shutil.copy(os.path.join(gamedir, 'OpenAL64.dll'),
                os.path.join(gamedir, 'jre/bin'))
