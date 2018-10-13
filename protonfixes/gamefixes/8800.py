""" Game fix for Civilization 4 (Beyond the Sword)
"""
#pylint: disable=C0103

import os
from protonfixes import util
from protonfixes.logger import log

def main():
    """ Install msxml3
    """

    log('Applying fixes for Civilization 4 (Beyond the Sword)')

    # https://github.com/ValveSoftware/Proton/issues/179#issuecomment-415593087
    util.protontricks('msxml3')
    util.protontricks('msxml4')
