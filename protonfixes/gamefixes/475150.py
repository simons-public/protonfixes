""" Game fix for Titan Quest Anniversary Edition(475150)
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Set OS to Windows XP to pass the black menu screen
    """

    log('Applying Titan Quest Anniversary Edition Game Fixes')

    util.protontricks('winxp')
