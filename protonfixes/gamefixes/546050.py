""" Game fix for Puyo Puyo Tetris
"""

#pylint: disable=C0103

from protonfixes import util
from protonfixes.protonversion import DeprecatedSince

@DeprecatedSince("5.0-3")
def main():
    """ Installs xact
    """

    util.protontricks('xact')
