""" Game fix for SkyDrift
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Use d9vk to avoid texture glitches
    """

    util.set_environment('PROTON_USE_D9VK', '1')
