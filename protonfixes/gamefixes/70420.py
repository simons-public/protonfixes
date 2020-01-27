""" Game fix for Chantelise - A Tale of Two Sisters
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Install directsound libraries
    """

    util.protontricks('dmime')
    util.protontricks('dmloader')
    util.protontricks('dmsynth')
    util.protontricks('dmusic')
    util.protontricks('dsound')
    util.protontricks('dswave')
    util.winedll_override('streamci', 'n')
    util.protontricks('sound=alsa')

    """ Fix for audio stutter/desync
    """
    util.set_environment('PULSE_LATENCY_MSEC', '60')
