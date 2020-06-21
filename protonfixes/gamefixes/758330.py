""" Game fix for Shenmue I & II
"""

#pylint: disable=C0103

from protonfixes import util

def main():
    """ Install dotnet46 so the launcher works and fix game audio.
    """

    # Install crypt32 (not required for Proton 3.16-3 and up)
    util.protontricks('dotnet46')

    # Install directmusic, set overrides
    util.winedll_override('xaudio2_7', 'n')
