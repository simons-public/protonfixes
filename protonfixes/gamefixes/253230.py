""" Game fix for A Hat in Time
"""

#pylint: disable=C0103

from protonfixes import util
from protonfixes.protonversion import DeprecatedSince

@DeprecatedSince("5.0-3")
def main():
    """ Enables D9VK
    """

    util.enable_d9vk()
