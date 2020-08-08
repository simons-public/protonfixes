""" Game fix for Duck Game
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ https://www.protondb.com/app/312530#bXY0Kuwwlz
    """
    util.winedll_override('dinput', 'n')
    util.append_argument('-nothreading')
