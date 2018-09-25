""" Game fox for Oddworld: Munch's Oddysee
Work in progress
"""
#pylint: disable=C0103


import sys


def main():
    """ Changes the proton argument from the launcher to the game
    """

    print('Applying Oddworld: Munch\'s Oddysee Game Fixes')

    # Replace launcher with game exe in proton arguments
    for idx, env in enumerate(sys.argv):
        if 'Launcher' in env:
            sys.argv[idx] = env.replace('bin/Launcher.exe', 'Munch.exe')

    print(sys.argv)
