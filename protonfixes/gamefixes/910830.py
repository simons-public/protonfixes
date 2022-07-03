""" Game fix for Rebel Galaxy Outlaw
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ installs mfc42
    """

    # https://github.com/ValveSoftware/Proton/issues/4216
    util.protontricks('mfc42')
