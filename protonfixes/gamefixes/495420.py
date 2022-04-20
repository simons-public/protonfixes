""" Game fix for State of Decay 2
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Fix game crashes with d3dcompiler_47 and multiplayer crashes with win7
    """

    util.protontricks('d3dcompiler_47')
    util.protontricks('win7')

