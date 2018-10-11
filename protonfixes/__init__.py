""" Starts the protonfix module
"""

import os
import sys
from . import fix

if 'DEBUG' in os.environ:
    from . import debug

fix.main()
