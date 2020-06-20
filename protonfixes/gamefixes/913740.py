""" Game fix for WORLD OF HORROR
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Disable esync
    """

    # esync causes occasional crashing
    util.set_environment('PROTON_NO_ESYNC', '1')
