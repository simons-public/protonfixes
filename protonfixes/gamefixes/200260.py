""" Game fix Batman Arkham City
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.protonversion import DeprecatedSince

@DeprecatedSince("5.0-3")
def main():
    """ Probably not needed when proton will be merged with newer wine
    """
    util.protontricks('dotnet20')
    util.protontricks('dotnet35')
    util.protontricks('physx')
    util.protontricks('mdx')
    util.protontricks('d3dcompiler_43')
    util.protontricks('d3dx9_43')
    util.protontricks('win10')
    util._mk_syswow64() #pylint: disable=protected-access

#TODO Checking possibly some tweak for language detection
