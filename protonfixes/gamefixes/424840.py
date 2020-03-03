""" Game fix for Little Nightmares
"""
# pylint: disable=C0103

import sys

def main():
    """ Add launch parameter
    """

    # The game crashes if running with more than one CPU thread,
    # adding "-onethread" will force the game to use only one CPU thread
    sys.argv.append('-onethread')
