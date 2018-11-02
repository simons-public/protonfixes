""" Starts the protonfix module
"""

import os
import sys
import traceback
from . import fix

if 'DEBUG' in os.environ:
    from . import debug

if 'STEAM_COMPAT_DATA_PATH' in os.environ:
    try:
        fix.main()

    #pylint: disable=W0702
    # Catch any exceptions and print a traceback
    except:
        sys.stderr.write('ProtonFixes ' + traceback.format_exc())
        sys.stderr.flush()
