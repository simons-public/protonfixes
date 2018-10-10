""" Starts the protonfix module
"""

import os
import sys
from . import fix

if 'DEBUG' in os.environ:
    from . import debug

if 'STEAMSCRIPT' in os.environ:
    if 'iscriptevaluator.exe' not in sys.argv[2]:
        fix.main()
