""" Utilities to make gamefixes easier
"""

import os
import glob
import subprocess

def which(appname):
    """ Returns the full path of an executable in $PATH
    """

    for path in os.environ['PATH'].split(os.pathsep):
        fullpath = os.path.join(path, appname)
        if os.path.exists(fullpath) and os.access(fullpath, os.X_OK):
            return fullpath
    print('%s not found in $PATH')
    return None

def protondir():
    """ Returns the path to proton
    """

    return glob.glob(os.path.join(
        os.environ['STEAM_COMPAT_CLIENT_INSTALL_PATH'],
        'steamapps/common/Proton*'))[0]

def protonprefix():
    """ Returns the wineprefix used by proton
    """

    return os.path.join(
        os.environ['STEAM_COMPAT_DATA_PATH'],
        'pfx/')

def protontricks(verb):
    """ Runes winetricks if available
    """

    env = dict(os.environ)
    env['WINEPREFIX'] = protonprefix()
    env['WINESERVER'] = os.path.join(protondir(), 'dist/bin/wine')

    winetricks_bin = which('winetricks')
    winetricks_cmd = [winetricks_bin] + verb.split(' ')

    print('Using winetricks', verb)
    if winetricks_bin is not None:
        process = subprocess.Popen(winetricks_cmd, env=env)
        process.wait()


def checkinstalled(verb):
    """ Returns True if the winetricks verb is found in the winetricks log
    """

    winetricks_log = os.path.join(protonprefix(), 'winetricks.log')
    try:
        with open(winetricks_log, 'r') as log:
            if verb in [x.strip() for x in log.readlines()]:
                return True
    except OSError:
        return False
