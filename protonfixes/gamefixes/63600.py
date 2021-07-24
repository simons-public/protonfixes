""" Game fix for realMyst
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Uses winetricks to install the icodecs verb
    """

    log('Applying fixes for realMyst')

    util.protontricks('icodecs')
