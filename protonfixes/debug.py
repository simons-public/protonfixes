""" Prints debug info if the environment variable DEBUG is 1
"""

import os
from future.utils import iteritems

print('\n\nEnvironment Variables:\n')

for key, value in iteritems(os.environ):
    print(key, '=', value)
