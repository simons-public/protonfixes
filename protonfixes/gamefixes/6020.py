""" Game fix for STAR WARS Jedi Knight - Jedi Academy
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Set Mesa env vars
    """

    log('Applying fixes for STAR WARS Jedi Knight - Jedi Academy')

    # https://github.com/ValveSoftware/Proton/pull/1423/commits/1a1d25c7d95691e37c94aea4e5f94e0c917aba6f
    util.set_environment('MESA_EXTENSION_MAX_YEAR', '2003')
    util.set_environment('__GL_ExtensionStringVersion', '17700')
