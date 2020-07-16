""" Game fix for Elite Dangerous
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Install dotnet40 and win7, as described in
        https://github.com/ValveSoftware/Proton/issues/150
    """
    util.protontricks('dotnet40')
    util.protontricks('win7')
