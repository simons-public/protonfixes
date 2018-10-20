""" Game fix for Doom 2016
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Install vcrun2015
    """

    # https://github.com/ValveSoftware/Proton/issues/788#issuecomment-416651267
    util.protontricks('vcrun2015')
