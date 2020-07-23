""" Game fix for Fallen Enchantress: Legendary Heroes
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Disable d9vk to avoid crash
        Disable SDNXLFonts.dll to render text
    """

    util.disable_dxvk()
    util.winedll_override('SDNXLFonts', 'd')
