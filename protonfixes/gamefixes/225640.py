""" Game fix for Sacred 2 Gold
"""
#pylint: disable=C0103

from protonfixes import util


def main():
    """ Install physx
    """

    util.protontricks('physx')
