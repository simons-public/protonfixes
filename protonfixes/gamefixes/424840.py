""" Game fix for Little Nightmares
"""
# pylint: disable=C0103

import sys
from protonfixes import util


def main():
    """ Install xact, override libraries and add launch parameter
    """

    # If proton Version is older than 3.16-5
    if util.protonversion(True) < 1544476838:
        # If not already installed, install xact
        util.protontricks('xact')

        # To fix audio crackling, set xaudio2_6.dll and xaudio2_7.dll to native
        util.winedll_override('xaudio2_6,xaudio2_7', 'n')

    # The game crashes if running with more than one CPU thread,
    # adding "-onethread" will force the game to use only one CPU thread
    sys.argv.append('-onethread')
