""" Game fix for The Evil Within(268050)
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Changes the proton argument from the launcher to the game
    """

    log('Applying The Evil Within Fixes')

    util.protontricks('xact')
    util.protontricks('win7')

    util.set_environment('PULSE_LATENCY_MSEC', '60')
