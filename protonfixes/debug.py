""" Prints debug info if the environment variable DEBUG is 1
"""

import os
import sys
from future.utils import iteritems

print('\n\nEnvironment Variables:\n')

for key, value in iteritems(os.environ):
    print(key, '=', value)

print('\n\nCommand Line:\n')
print(sys.argv)

print('\n\nVersion:\n')
print(sys.version)
