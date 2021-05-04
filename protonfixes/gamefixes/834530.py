""" Game fix for Yakuza Kiwami
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Disable FSYNC
    """

    # Disable fsync to fix saving issues and hang on exit
    util.disable_fsync()
