""" Game fix for Toybox Turbos
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Changes the proton argument from the launcher to the game
    """

    log('Applying fixes for Toybox Turbos')

    # Fix infinite startup screen
    util.set_environment('PROTON_NO_ESYNC', '1')
