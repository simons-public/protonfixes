""" Prints debug info if the environment variable DEBUG is 1
"""

import os
import sys
import shutil
# pylint: disable=E0611
from __main__ import CURRENT_PREFIX_VERSION, basedir, env

def log(msg=None):
    pfx = 'ProtonFixes[' + str(os.getpid()) + '] DEBUG: '
    sys.stderr.write(pfx + str(msg) +  os.linesep)
    sys.stderr.flush()

line = '---------------------------------------'
log('---- begin protontricks debug info ----')
log('Proton Python Version:')
log(sys.executable)
log(sys.version)
log(line)
log('System Python Version:')
try:
    log(shutil.which(os.readlink(shutil.which('python'))))
except:
    log(shutil.which('python'))
log(line)

log('Proton Version:')
log(CURRENT_PREFIX_VERSION)
log(line)

log('Proton Directory:')
log(basedir)
log(line)

ignorevars = ['SteamUser', 'OLDPWD', 'SDL_GAMECONTROLLERCONFIG', 'SteamAppUser', 'SDL_GAMECONTROLLER_IGNORE_DEVICES']
log('Environment Variables:')
for key, value in os.environ.items():
    if key not in ignorevars:
        log(key + '=' + value)
log(line)

log('Command Line:')
log(sys.argv)
log('----- end protontricks debug info -----')
