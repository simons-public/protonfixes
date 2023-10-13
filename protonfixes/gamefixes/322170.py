""" Game fixs for Geometry Dash
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log

def main():
    """ Changes the proton argument from the launcher to the game
    """

    log('Applying fixes for Geometry Dash')

    # Fix FSYNC and ESYNC being enabled
    util.set_environment('PROTON_NO_ESYNC', '1')
    util.set_environment('PROTON_NO_FSYNC', '1')

    # Me when single-core games:
    util.append_argument('-USEALLAVAILABLECORES')

    # Geode compatibility go brrrr
    util.winedll_override('xinput9_1_0', 'n', 'b')
