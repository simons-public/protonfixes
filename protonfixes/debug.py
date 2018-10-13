""" Prints debug info if the environment variable DEBUG is 1
"""

import os
import sys
import shutil
# pylint: disable=E0611
from __main__ import CURRENT_PREFIX_VERSION, basedir
from .logger import log

os.environ['DEBUG'] = '1'

LINE = '---------------------------------------'
log.debug('---- begin protontricks debug info ----')
log.debug('Proton Python Version:')
log.debug(sys.executable)
log.debug(sys.version)
log.debug(LINE)
log.debug('System Python Version:')
try:
    log.debug(shutil.which(os.readlink(shutil.which('python'))))
except: #pylint: disable=W0702
    log.debug(shutil.which('python'))
log.debug(LINE)

log.debug('Proton Version:')
log.debug(CURRENT_PREFIX_VERSION)
log.debug(LINE)

log.debug('Proton Directory:')
log.debug(basedir)
log.debug(LINE)

IGNOREVARS = [
    'SteamUser',
    'OLDPWD',
    'SDL_GAMECONTROLLERCONFIG',
    'SteamAppUser',
    'SDL_GAMECONTROLLER_IGNORE_DEVICES',
    'LS_COLORS',
]

log.debug('Environment Variables:')
for key, value in os.environ.items():
    if key not in IGNOREVARS:
        log.debug(key + '=' + value)
log.debug(LINE)

log.debug('Command Line:')
log.debug(sys.argv)
log.debug('----- end protontricks debug info -----')
