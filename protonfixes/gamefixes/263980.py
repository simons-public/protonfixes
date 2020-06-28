""" Game fix for Out There Somewhere
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Bypass launcher, disable dxvk
    """

    util.replace_command('ots.exe', 'ots_executable.exe')
    util.disable_dxvk()
