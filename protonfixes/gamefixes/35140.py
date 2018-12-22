""" Game fix Batman Arkham Asylum
    (Currently no contollers)
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    #Probably not needed when proton will be merged with newer wine
    util.use_win32_prefix()
    util.protontricks('winxp')
    util.protontricks('dotnet20')
    util.protontricks('dotnet35')
    util.protontricks('physx')
    util.protontricks('mdx')
    util.protontricks('d3dx9')
    util.protontricks('d3dcompiler_43')
    util._mk_syswow64()
#TODO Controllers fixes 
