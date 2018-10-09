""" Utilities to make gamefixes easier
"""

import os
import sys
import glob
import shutil
import signal
import subprocess

# pylint: disable=I1101, W0101

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
    
    try:
        proton_dir = glob.glob(os.path.join(
            os.environ['STEAM_COMPAT_CLIENT_INSTALL_PATH'],
            'steamapps/common/Proton*'))[0]
        return proton_dir
    except IndexError:
        base = '/'.join(env['STEAM_COMPAT_DATA_PATH'].split('/')[:-2])
        proton_dir = glob.glob(os.path.join(
            base, 'common/Proton*'))[0]
        return proton_dir


def protonprefix():
    """ Returns the wineprefix used by proton
    """

    return os.path.join(
        os.environ['STEAM_COMPAT_DATA_PATH'],
        'pfx/')


def _killhanging():
    """ Kills processes that hang when installing winetricks
    """

    # avoiding an external library as proc should be available on linux
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
    badexes = ['mscorsvw.exe']
    for pid in pids:
        try:
            with open(os.path.join('/proc', pid, 'cmdline'), 'rb') as proc_cmd:
                cmdline = proc_cmd.read()
                for exe in badexes:
                    if exe in cmdline.decode():
                        os.kill(int(pid), signal.SIGKILL)
        except IOError:
            continue


def protontricks(verb):
    """ Runs winetricks if available
    """

    if not checkinstalled(verb):
        env = dict(os.environ)
        env['WINEPREFIX'] = protonprefix()
        env['WINESERVER'] = os.path.join(protondir(), 'dist/bin/wineserver')

        winetricks_bin = which('winetricks')
        winetricks_cmd = [winetricks_bin, '--unattended', '--force'] + verb.split(' ')
        wineserver_bin = env['WINESERVER']

        if winetricks_bin is not None:

            # winetricks relies entirely on the existence of syswow64 to determine
            # if the prefix is 64 bit, while proton fails to run without it
            if 'win32' in protonprefix():
                try:
                    shutil.rmtree(os.path.join(protonprefix(), 'drive_c/windows/syswow64'))
                except FileNotFoundError:
                    pass

            # make sure proton waits for winetricks to finish
            for idx, arg in enumerate(sys.argv):
                if 'waitforexitandrun' not in arg:
                    sys.argv[idx] = arg.replace('run', 'waitforexitandrun')

            print('Using winetricks', verb)
            process = subprocess.Popen(winetricks_cmd, env=env)
            process.wait()
            _killhanging()
            subprocess.Popen([wineserver_bin, '-k'], env=env)
            return True

            # restore syswow64 so proton doesn't crash
            if 'win32' in protonprefix():
                try:
                    os.makedirs(os.path.join(protonprefix(), 'drive_c/windows/syswow64'))
                except FileExistsError:
                    pass

    return False


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
    return False


def win32_prefix_exists():
    """ Returns True if there is a _win32 path available
    """

    prefix32 = os.environ['STEAM_COMPAT_DATA_PATH'] + '_win32/pfx'
    if os.path.exists(prefix32):
        return True
    return False


def use_win32_prefix():
    """ Sets variables in the main proton script to use the _win32 prefix
    """
    if not win32_prefix_exists():
        make_win32_prefix()

    import __main__ as protonmain
    data_path = os.environ['STEAM_COMPAT_DATA_PATH'] + '_win32'
    prefix32 = os.environ['STEAM_COMPAT_DATA_PATH'] + '_win32/pfx/'

    protonmain.env['STEAM_COMPAT_DATA_PATH'] = data_path
    protonmain.env['WINEPREFIX'] = prefix32
    protonmain.env['WINEDLLPATH'] = os.path.join(protondir(), 'dist/lib/wine')
    protonmain.env['WINEARCH'] = 'win32'
    protonmain.prefix = prefix32

    os.environ['STEAM_COMPAT_DATA_PATH'] = data_path
    os.environ['WINEPREFIX'] = prefix32
    os.environ['WINEDLLPATH'] = os.path.join(protondir(), 'dist/lib/wine')
    os.environ['WINEARCH'] = 'win32'

    # make sure steam doesn't crash when missing syswow
    try:
        os.makedirs(os.path.join(prefix32, 'drive_c/windows/syswow64'))
    except FileExistsError:
        pass


def make_win32_prefix():
    """ Creates a win32 prefix
    """

    env = dict(os.environ)
    print('Bootstrapping win32 prefix')

    prefix32 = os.environ['STEAM_COMPAT_DATA_PATH'] + '_win32/pfx'
    try:
        os.makedirs(prefix32)

        env['WINEARCH'] = 'win32'
        env['WINEPREFIX'] = prefix32
        server = subprocess.Popen([which('wineserver'), '-f'], env=env)
        subprocess.Popen([which('wine'), 'wineboot', '--init'], env=env)
        server.wait()

        os.makedirs(os.path.join(prefix32, 'drive_c/windows/syswow64'))
        os.symlink(
            os.path.join(prefix32, 'drive_c/Program Files'),
            os.path.join(prefix32, 'drive_c/Program Files (x86)'))

        print('Initialized win32 prefix')

    except OSError:
        print('Directory for win32 prefix already exists')


def replace_command(orig_str, repl_str):
    """ Make a commandline replacement in sys.argv
    """

    for idx, arg in enumerate(sys.argv):
        if orig_str in arg:
            sys.argv[idx] = arg.replace(orig_str, repl_str)

def append_argument(argument):
    """ Append an argument to sys.argv
    """

    sys.argv.append(argument)
