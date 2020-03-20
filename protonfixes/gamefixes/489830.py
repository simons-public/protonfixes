""" Game fix for The Elder Scrolls V: Skyrim Special Edition
"""
#pylint: disable=C0103

from protonfixes import util


def main():
    """ Install FAudio for NPC dialog audio
    """

    # Source: https://github.com/ValveSoftware/Proton/issues/4
    util.protontricks('faudio')
