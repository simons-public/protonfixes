""" Game fix for Doom 2016
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Install vcrun2015
    """

    # https://github.com/ValveSoftware/Proton/issues/788#issuecomment-416651267
    util.protontricks('vcrun2015')
