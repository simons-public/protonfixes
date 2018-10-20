""" Game fix for Killer is Dead at Launch
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Installs dotnet45 directx9 vcruntime2010 and xact_june2018 and sets to winxp
    """

    # https://github.com/ValveSoftware/Proton/issues/1387#issuecomment-428059647
    util.protontricks('winxp')
    util.protontricks('dotnet45')
    util.protontricks('directx9')
    util.protontricks('vcruntime2010')
    util.protontricks('xact_june2018')
