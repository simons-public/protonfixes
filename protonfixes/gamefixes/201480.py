""" Game fix for Serious Sam: The Random Encounter
"""
#pylint: disable=C0103

from protonfixes import util


def main():
    """ Installs directmusic and directplay
    """

    util.protontricks('dmband')
    util.protontricks('dmime')
    util.protontricks('dmloader')
    util.protontricks('dmsynth')
    util.protontricks('dmstyle')
    util.protontricks('dmusic')
    util.protontricks('dsound')
    util.protontricks('dswave')
    util.protontricks('directplay')
    util.winedll_override('streamci', 'n')
