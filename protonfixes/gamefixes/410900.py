""" Game fix for Forts
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Uses winetricks to install the ole32 verb
    """

    util.protontricks('ole32')
