""" Game fix for Grand Theft Auto V
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Install corefonts
    """

    log('Applying fixes for Grand Theft Auto V')

    # https://github.com/ValveSoftware/Proton/issues/37
    util.protontricks('corefonts')
