""" Game fix for Spacewar
"""
# pylint: disable=C0103
from protonfixes import util


def main():
    """ Install d3d9x
    """

    print('Applying fixes for Spacewar')

    # The game needs d3d9x, otherwise no fonts will be rendered.
    util.protontricks('d3d9x')
