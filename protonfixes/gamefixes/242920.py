""" Game fix for Banished
"""
# pylint: disable=C0103
import os
import sys
from protonfixes import util


def main():
    """ Install xact and override
    """

    print('Applying fixes for Banished')

    # If not already installed, install xact
    if not util.checkinstalled('xact'):
        util.protontricks('xact')

    # Set xaudio2_7 to native, otherwise audio won't work
    util.winedll_override('xaudio2_7', 'n')
