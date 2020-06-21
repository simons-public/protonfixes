""" Game fix for Borderlands GOTY Enhanced
"""
#pylint: disable=C0103

import os

from protonfixes import util
from protonfixes.logger import log


def main():
    """ Uses dotnet40
    """

    util.protontricks('dotnet40')

    # Allow setting an environment variable to prevent replacing the launcher
    # just in case one day the launcher works (at which point we can remove the below
    # fixes).
    log.info("Checking if we should keep launcher...")
    if 'KEEP_LAUNCHER' in os.environ:
        log.info("KEEP_LAUNCHER is set so keeping the original launch command.")
        return True

    log.info("KEEP_LAUNCHER is not set so replacing the launcher with the "
             "game executable in the launch command.")

    util.replace_command('Launcher.exe', 'BorderlandsGOTY.exe')
    return True
