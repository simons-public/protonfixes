""" Starts the protonfix module
"""

import os
import sys
from . import fix

if 'DEBUG' in os.environ:
    from . import debug

if 'STEAM_COMPAT_DATA_PATH' in os.environ:
    fix.main()
