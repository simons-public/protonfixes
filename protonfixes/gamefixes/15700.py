""" Game fix for Oddworld: Abe's Oddysee
TODO: Fix steam controller input, it is stuck in lizard mode without overlay
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Adds the -interline argument to the game
    """

    log('Applying fixes for Oddworld: Abe\'s Oddysee')

    # Adding -interline fixes slow videos but adds scanlines
    util.append_argument('-interline')
