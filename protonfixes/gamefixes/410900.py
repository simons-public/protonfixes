""" Game fix for Forts
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Uses winetricks to install the ole32 verb
    """

    print('Applying fixes for Forts')

    util.protontricks('ole32')
