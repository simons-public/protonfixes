""" Game fix for Night of the Full Moon
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Use 32-bit version
    """
    util.replace_command('Night of the Full Moon.exe', 'x86/Night of the Full Moon.exe')
