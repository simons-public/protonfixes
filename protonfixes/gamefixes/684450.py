""" Game fix for Surviving the Aftermath
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Launcher currently broken
    """
    util.replace_command("launcher/Paradox Launcher.exe", "Aftermath64.exe")
