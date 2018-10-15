""" Game fix for SUGURI 2
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Installs d3dxof
    """

    log('Applying fixes for SUGURI 2')

    # https://github.com/ValveSoftware/Proton/issues/970#issuecomment-420421289
    util.protontricks('d3dxof')
