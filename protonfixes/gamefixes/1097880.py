""" Game fix for Super Naughty Maid 2
"""

from protonfixes import util


def main():
    """ installs quartz, wmp9
    """

    util.use_win32_prefix()

    # The whole game is only videos and require wmp9 & quartz
    util.protontricks('quartz')
    util.protontricks('wmp9')
