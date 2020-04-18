""" Game fix for Watch_Dogs
"""
# pylint: disable=C0103
import subprocess
from protonfixes import util
from protonfixes import splash


def main():
    """ Fix the in-game sound
    """

    util.protontricks('xact')
    util.protontricks('winxp')

    info_popup()


@util.once
def info_popup():
    """ Show info popup on first run
    """
    zenity_bin = splash.sys_zenity_path()
    if not zenity_bin:
        return
    # pylint: disable=C0301
    zenity_cmd = ' '.join([
        zenity_bin,
        '--info',
        '--text',
        '"If the game does not run the first time and complains that the UPlay launcher\nis not compatible with the operating system: cancel and restart the game."',
        '--no-wrap'])
    subprocess.Popen(zenity_cmd, shell=True)
