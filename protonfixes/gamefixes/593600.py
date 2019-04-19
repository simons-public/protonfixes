""" Game fix for PixARK
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Overrides the mprapi.dll to native.
    """

    util.winedll_override('mprapi', 'x')
