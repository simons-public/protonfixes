""" Game fix for Borderlands: The Pre-Sequel
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Launcherfix
    """

    # Fixes the startup process.
    util.replace_command('Launcher.exe', 'BorderlandsPreSequel.exe')
    util.append_argument('-NoSplash')
