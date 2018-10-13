""" Game fix for Tesla Effect
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Install corefonts
    """

    log('Applying fixes for Tesla Effect')

    # https://github.com/ValveSoftware/Proton/issues/1317
    util.protontricks('corefonts')
