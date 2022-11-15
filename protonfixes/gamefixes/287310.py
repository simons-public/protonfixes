""" Game fix for Re-Volt (287310)
"""

#pylint: disable=C0103

from protonfixes import util

def main():
    """ Sets the necessary dll overrides for the wrappers that are shipped with the game
    """

    # Set overrides
    util.winedll_override('ddraw', 'n')
    util.winedll_override('dinput', 'n')
