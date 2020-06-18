""" Game fix for Sonic Generations Collection
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Disable ESYNC/FSYNC
    """

    # Disables esync/fsync to fix sound.
    util.disable_esync()
    util.disable_fsync()
