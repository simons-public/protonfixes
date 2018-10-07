""" Starts the protonfix module
"""

import os
if 'STEAMSCRIPT' in os.environ:
    if 'DEBUG' in os.environ:
        from . import debug
        from . import fix
    else:
        from . import fix
