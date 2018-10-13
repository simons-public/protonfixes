""" Game fix for EVE Online
"""
#pylint: disable=C0103

import os
from protonfixes import util
from protonfixes.logger import log

def main():
    """ Set to winxp
    """

    log('Applying fixes for EVE Online')

    # https://github.com/ValveSoftware/Proton/issues/1223#issue-356628050
    util.protontricks('winxp')
