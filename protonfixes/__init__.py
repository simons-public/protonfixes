""" Starts the protonfix module
"""

import os
if 'DEBUG' in os.environ:
    from . import debug
    from . import fix
else:
    from . import fix
