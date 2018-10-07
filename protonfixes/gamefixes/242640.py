""" Game fix for Styx: Master of Shadows
"""
#pylint: disable=C0103


from protonfixes import util


def main():
    """ Install dotnet40
    """

    print('Applying fixes for Styx: Master of Shadows')

    util.protontricks('dotnet40')
