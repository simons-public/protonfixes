""" Game fix for FINAL FANTASY IX
"""
#pylint: disable=C0103

import os
from protonfixes import util
from protonfixes.logger import log

def main():
    """ Changes the proton argument from the launcher to the game
    """

    log('Applying fixes for FINAL FANTASY IX')

    # Fix crackling audio
    os.environ['PULSE_LATENCY_MSEC'] = '60'

    # Replace launcher with game exe in proton arguments
    util.replace_command('FF9_Launcher.exe', 'x64/FF9.exe')
