""" Game fix for Order of Battle: World War II
Still missing intro video codecs
"""
#pylint: disable=C0103

import os
from protonfixes import util
from protonfixes.logger import log

def main():
    """ Install corefonts
    """

    log('Applying fixes for Order of Battle: World War II')

    # https://github.com/ValveSoftware/Proton/issues/639
    util.protontricks('corefonts')
