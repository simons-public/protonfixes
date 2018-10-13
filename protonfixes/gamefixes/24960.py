""" Game fix for Battlefield: Bad Company 2
"""
#pylint: disable=C0103

import os
from protonfixes import util
from protonfixes.logger import log

def main():
    """ Install corefonts, dx9. Set to win7 and override msdmo
    """

    log('Applying fixes for Battlefield: Bad Company 2')

    # https://github.com/ValveSoftware/Proton/issues/200#issuecomment-415905979
    util.protontricks('win7')
    util.protontricks('corefonts')
    util.protontricks('directx9')
    os.environ['WINEDLLOVERRIDES'] = 'msdmo=b'
