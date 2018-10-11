""" Game fix for Styx: Master of Shadows
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Install dotnet40
    Works, but gives a popup twice at the beginning of launch:
    'Unable to find a version of the runtime to run this
    application. (OK)
    """

    log('Applying fixes for Styx: Master of Shadows')

    # https://github.com/ValveSoftware/Proton/issues/810
    # https://steamcommunity.com/app/242640/discussions/0/620700960990638817/
    util.protontricks('xact')
    util.protontricks('dotnet40')
