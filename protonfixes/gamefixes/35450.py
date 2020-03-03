""" Game fix for Rising Storm/Red Orchestra 2 Multiplayer
"""
# pylint: disable=C0103
from protonfixes import util
from protonfixes.protonversion import DeprecatedSince

@DeprecatedSince("5.0-3")
def main():
    """ Install xact
    """

    print('Applying fixes for Rising Storm/Red Orchestra 2 Multiplayer')

    # Unreal Engine games needs xact, otherwise all audio will be playing at equal loudness.
    # https://github.com/ValveSoftware/Proton/issues/54
    # https://github.com/ValveSoftware/Proton/issues/155
    util.protontricks('xact')
