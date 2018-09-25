""" Game fix for FINAL FANTASY IX
"""
#pylint: disable=C0103


import os
import sys


def main():
    """ Changes the proton argument from the launcher to the game
    """

    print('Applying FINAL FANTASY IX Game Fixes')

    # Fix crackling audio
    os.environ['PULSE_LATENCY_MSEC'] = '60'

    # Replace launcher with game exe in proton arguments
    for idx, env in enumerate(sys.argv):
        if 'FF9_Launcher' in env:
            sys.argv[idx] = env.replace('FF9_Launcher.exe', 'x64/FF9.exe')
