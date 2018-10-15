""" Game fix for The Evil Within(268050)
"""
#pylint: disable=C01033

import os
from protonfixes import util
from protonfixes.logger import log

def main():
    """ Changes the proton argument from the launcher to the game
    """

    log('Applying The Evil Within Fixes')

    util.protontricks('win7')

    os.environ['PULSE_LATENCY_MSEC'] = '60'
    util.protontricks('xact')
