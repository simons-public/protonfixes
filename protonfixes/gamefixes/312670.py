""" Game fix for Strange Brigade
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ This bypasses Strange Brigade's Launcher, which renders all black.
    """

    # Fixes the startup process.
    util.replace_command('StrangeBrigade.exe', 'StrangeBrigade_Vulkan.exe')
    util.append_argument('-skipdrivercheck -noHDR')
