""" Game fix for Might & Magic: Heroes VII - Trial by Fire
"""

#pylint: disable=C0103

from protonfixes import util

def main():
    """ Install uplay
    """

    # Install uplay
    util.protontricks('uplay')
