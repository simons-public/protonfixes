""" Game fix for Yakuza 0
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Disable FSYNC
    """

    # Disable fsync to fix saving issues
    util.disable_fsync()
