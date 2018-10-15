""" Game fix for Age of Empires 2 HD Edition
Source: https://github.com/JamesHealdUK/protonfixes/blob/master/fixes/221380.sh
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Changes the proton argument from the launcher to the game
    """

    log('Applying fixes for Age of Empires 2 HD Edition')

    # Replace launcher with game exe in proton arguments
    util.replace_command('Launcher.exe', 'AoK HD.exe')
