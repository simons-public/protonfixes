""" Game fix Stealth Inc 2: A Game of Clones
"""
# pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log


def main():
    """ dsound is needed for audio
    """

    log('Installing dsound')
    util.protontricks('dsound')
