""" Game fix for Sniper Elite 3 ""
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Changes the proton argument from the launcher to the game
    """

    log('Applying fixes for Sniper Elite 3')
    
    util.replace_command('Launcher/Sniper3Launcher.exe', 'bin/SniperElite3.exe')
