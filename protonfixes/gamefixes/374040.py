""" Game fix for Portal Knights
"""
# pylint: disable=C0103
from protonfixes import util


def main():
    """ Install xact and override xaudio2_7 to native
    """

    print('Applying fixes for Portal Knights')

    # install xact
    util.protontricks('xact')

    # set xaudio2_7.dll to native
    util.winedll_override('xaudio2_7', 'n')
