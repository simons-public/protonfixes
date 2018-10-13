""" Game fix for You Need a Budget 4
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Installs corefonts
    """

    log('Applying fixes for You Need a Budget 4')

    # https://github.com/ValveSoftware/Proton/issues/7
    util.protontricks('corefonts')
