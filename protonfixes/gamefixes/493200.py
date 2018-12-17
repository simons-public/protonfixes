""" Game fix for RiME
"""

# pylint: disable=C0103

from protonfixes import util


def main():
    """ Install xact and dinput8, override libraries and disable esync
    """

    print('Applying fixes for RiME')

    # if Proton version older than 3.16-5
    if util.protonversion(True) < 1544476838:
        # If not already installed, install xact
        util.protontricks('xact')

        # To fix audio crackling, set xaudio2_7.dll to native
        util.winedll_override('xaudio2_7', 'n')

    # Gamepad doesn't work properly without dinput8 installed
    util.protontricks('dinput8')

    # To fix gamepad set dinput8 to native
    util.winedll_override('dinput8', 'n')

    # disable esync to prevent game crash after a few minutes
    util.disable_esync()
