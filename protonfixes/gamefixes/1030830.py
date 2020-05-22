""" Game fix for Mafia II: Definitive Edition ""
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Changes the proton argument from the launcher to the game
    """

    log('Applying fixes for Mafia II: Definitive Edition')

    util.protontricks('dotnet542')
    util.replace_command('Launcher.exe', '../Mafia II Definitive Edition.exe')
