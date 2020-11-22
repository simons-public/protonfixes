""" Game fix Age of Wonders: Planetfall
"""
#pylint: disable=C0103

from protonfixes import util


def main():
    """ Changes the proton argument from the launcher to the game
    """

    # Replace launcher with game exe in proton arguments
    util.replace_command('dowser.exe', 'AowPF.exe')
