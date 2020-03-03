""" Game fix for Titan Quest Anniversary Edition(475150)
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.protonversion import DeprecatedSince

@DeprecatedSince("5.0-3")
def main():
    """ Set OS to Windows XP to pass the black menu screen
    """

    util.protontricks('winxp')
