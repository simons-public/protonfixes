""" Game fix for RiME
"""

# pylint: disable=C0103

from protonfixes import util


def main():
    """ Install xact and dinput8, override libraries and disable esync
    """

    print('Applying fixes for RiME')

    # If not already installed, install xact
    if not util.checkinstalled('xact'):
        util.protontricks('xact')

    # Gamepad doesn't work properly without dinput8 installed
    if not util.checkinstalled('dinput8'):
        util.protontricks('dinput8')

    # To fix audio crackling, set xaudio2_7.dll to native
    # To fix gamepad set dinput8 to native
    util.winedll_override('xaudio2_7,dinput8', 'n')

    # disable esync to prevent game crash after a few minutes
    util.disable_esync()
