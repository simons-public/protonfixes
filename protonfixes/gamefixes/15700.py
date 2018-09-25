""" Game fox for Oddworld: Abe's Oddysee
TODO: Fix steam controller input, it is stuck in lizard mode without overlay
"""
#pylint: disable=C0103


import sys


def main():
    """ Adds the -interline argument to the game
    """

    print('Applying Oddworld: Abe\'s Oddysee Fixes')

    # Adding -interline fixes slow videos but adds scanlines
    sys.argv.append('-interline')
