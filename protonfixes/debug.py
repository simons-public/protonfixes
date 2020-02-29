""" Prints debug info if the environment variable DEBUG is 1
"""

import os
import sys
import shutil
# pylint: disable=E0611
from .protonmain_compat import protonmain
from .protonversion import PROTON_VERSION
from .logger import log

os.environ['DEBUG'] = '1'

def show_debug_info():
    """ Show various debug info """

    check_args = [
        'iscriptevaluator.exe' in sys.argv[2],
        'getcompatpath' in sys.argv[1],
        'getnativepath' in sys.argv[1],
    ]

    if any(check_args):
        log.debug(str(sys.argv))
        return

    line = '---------------------------------------'
    log.debug('---- begin protontricks debug info ----')
    log.debug('Proton Python Version:')
    log.debug(sys.executable)
    log.debug(sys.version)
    log.debug(line)
    log.debug('System Python Version:')
    try:
        log.debug(shutil.which(os.readlink(shutil.which('python'))))
    except: #pylint: disable=W0702
        log.debug(shutil.which('python'))
    log.debug(line)

    log.debug('Proton Version:')
    log.debug(PROTON_VERSION)
    log.debug(line)

    log.debug('Proton Directory:')
    log.debug(protonmain.g_proton.base_dir)
    log.debug(line)

    ignorevars = [
        'SteamUser',
        'OLDPWD',
        'SteamAppUser',
        'LS_COLORS',
    ]

    log.debug('Environment Variables:')
    for key, value in os.environ.items():
        if key not in ignorevars:
            log.debug(key + '=' + value)
    log.debug(line)

    log.debug('Command Line:')
    log.debug(sys.argv)
    log.debug('----- end protontricks debug info -----')

show_debug_info()
