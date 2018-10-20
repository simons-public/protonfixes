""" Utilities to make gamefixes easier
"""

import configparser
import os
import sys
import shutil
import signal
import subprocess
from .logger import log
try:
    import __main__ as protonmain
except ImportError:
    log.warn('Unable to hook into Proton main script environment')

# pylint: disable=unreachable

def which(appname):
    """ Returns the full path of an executable in $PATH
    """

    for path in os.environ['PATH'].split(os.pathsep):
        fullpath = os.path.join(path, appname)
        if os.path.exists(fullpath) and os.access(fullpath, os.X_OK):
            return fullpath
    log.warn(str(appname) + 'not found in $PATH')
    return None


def protondir():
    """ Returns the path to proton
    """

    proton_dir = os.path.dirname(sys.argv[0])
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
    log.debug('Killing hanging wine processes')
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

def _del_syswow64():
    """ Deletes the syswow64 folder
    """

    try:
        shutil.rmtree(os.path.join(protonprefix(), 'drive_c/windows/syswow64'))
    except FileNotFoundError:
        log.warn('The syswow64 folder was not found')

def _mk_syswow64():
    """ Makes the syswow64 folder
    """

    try:
        os.makedirs(os.path.join(protonprefix(), 'drive_c/windows/syswow64'))
    except FileExistsError:
        log.warn('The syswor64 folder already exists')


def checkinstalled(verb):
    """ Returns True if the winetricks verb is found in the winetricks log
    """

    if not isinstance(verb, str):
        return False

    log.info('Checking if winetricks ' + verb + ' is installed')
    winetricks_log = os.path.join(protonprefix(), 'winetricks.log')
    try:
        with open(winetricks_log, 'r') as tricklog:
            if verb in [x.strip() for x in tricklog.readlines()]:
                return True
    except OSError:
        return False
    return False


def protontricks(verb):
    """ Runs winetricks if available
    """

    if not checkinstalled(verb):
        log.info('Installing winetricks ' + verb)
        env = dict(protonmain.env)
        env['WINEPREFIX'] = protonprefix()
        env['WINE'] = protonmain.wine_path
        env['WINELOADER'] = protonmain.wine_path
        env['WINESERVER'] = os.path.join(protonmain.bindir, 'wineserver')
        env['WINETRICKS_LATEST_VERSION_CHECK'] = 'disabled'

        winetricks_bin = which('winetricks')
        winetricks_cmd = [winetricks_bin, '--unattended', '--force'] + verb.split(' ')

        if winetricks_bin is None:
            log.warn('No winetricks was found in $PATH')

        if winetricks_bin is not None:

            log.debug('Using winetricks command: ' + str(winetricks_cmd))
            # winetricks relies entirely on the existence of syswow64 to determine
            # if the prefix is 64 bit, while proton fails to run without it
            log.debug('Deleting syswow64')
            if 'win32' in protonprefix():
                _del_syswow64()

            # make sure proton waits for winetricks to finish
            for idx, arg in enumerate(sys.argv):
                if 'waitforexitandrun' not in arg:
                    sys.argv[idx] = arg.replace('run', 'waitforexitandrun')
                    log.debug(str(sys.argv))

            log.info('Using winetricks verb ' + verb)
            process = subprocess.Popen(winetricks_cmd, env=env)
            process.wait()
            _killhanging()
            log.info('Winetricks complete')
            return True

            # restore syswow64 so proton doesn't crash
            log.info('Restoring syswow64 folder')
            if 'win32' in protonprefix():
                _mk_syswow64()
    return False


def win32_prefix_exists():
    """ Returns True if there is a _win32 path available
    """

    prefix32 = os.environ['STEAM_COMPAT_DATA_PATH'] + '_win32/pfx'
    if os.path.exists(prefix32):
        log.debug('Found win32 prefix')
        return True
    log.debug('No win32 prefix found')
    return False


def use_win32_prefix():
    """ Sets variables in the main proton script to use the _win32 prefix
    """
    if not win32_prefix_exists():
        make_win32_prefix()

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
    log.debug('Updated environment variables for win32 prefix')
    # make sure steam doesn't crash when missing syswow
    try:
        os.makedirs(os.path.join(prefix32, 'drive_c/windows/syswow64'))
    except FileExistsError:
        pass


def make_win32_prefix():
    """ Creates a win32 prefix
    """

    env = dict(os.environ)
    log.info('Bootstrapping win32 prefix')

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

        log.info('Initialized win32 prefix')

    except OSError:
        log.warn('Directory for win32 prefix already exists')


def replace_command(orig_str, repl_str):
    """ Make a commandline replacement in sys.argv
    """

    log.info('Changing ' + orig_str + ' to ' + repl_str)
    for idx, arg in enumerate(sys.argv):
        if orig_str in arg:
            sys.argv[idx] = arg.replace(orig_str, repl_str)

def append_argument(argument):
    """ Append an argument to sys.argv
    """

    log.info('Adding argument ' + argument)
    sys.argv.append(argument)
    log.debug('New commandline: ' + str(sys.argv))

def set_environment(envvar, value):
    """ Add or override an environment value
    """

    log.info('Adding env: ' + envvar + '=' + value)
    os.environ[envvar] = value
    protonmain.env[envvar] = value

def get_game_install_path():
    """ Game installation path
    """

    log.debug('Detected path to game: ' + os.environ['PWD'])
    # only for `waitforexitandrun` command
    return os.environ['PWD']

def winedll_override(dll, dtype):
    """ Add WINE dll override
    """

    log.info('Overriding ' + dll + '.dll = ' + dtype)
    protonmain.dlloverrides[dll] = dtype

def disable_nvapi():
    """ Disable WINE nv* dlls
    """

    log.info('Disabling NvAPI')
    winedll_override('nvapi', '')
    winedll_override('nvapi64', '')
    winedll_override('nvcuda', '')
    winedll_override('nvcuvid', '')
    winedll_override('nvencodeapi', '')
    winedll_override('nvencodeapi64', '')

def disable_d3d10():
    """ Disable WINE d3d10* dlls
    """

    log.info('Disabling d3d10')
    winedll_override('d3d10', '')
    winedll_override('d3d10_1', '')
    winedll_override('d3d10core', '')

def disable_dxvk():  # pylint: disable=missing-docstring
    set_environment('PROTON_USE_WINED3D11', '1')

def disable_esync():  # pylint: disable=missing-docstring
    set_environment('PROTON_NO_ESYNC', '1')

def disable_d3d11():  # pylint: disable=missing-docstring
    set_environment('PROTON_NO_D3D11', '1')


def create_dosbox_conf(conf_file, conf_dict):
    """Create DOSBox configuration file.

    DOSBox accepts multiple configuration files passed with -conf
    option;, each subsequent one overwrites settings defined in
    previous files.
    """
    if os.access(conf_file, os.F_OK):
        return
    conf = configparser.ConfigParser()
    conf.read_dict(conf_dict)
    with open(conf_file, 'w') as file:
        conf.write(file)


def read_dxvk_conf(cfp):
    """ Add fake [DEFAULT] section to dxvk.conf
    """
    yield '['+ configparser.ConfigParser().default_section +']'
    yield from cfp


def set_dxvk_option(opt, val, cfile='/tmp/protonfixes_dxvk.conf'):
    """ Create custom DXVK config file

    See https://github.com/doitsujin/dxvk/wiki/Configuration for details
    """
    conf = configparser.ConfigParser()
    conf.optionxform = str
    section = conf.default_section
    dxvk_conf = os.path.join(get_game_install_path(), 'dxvk.conf')

    conf.read(cfile)

    if not conf.has_option(section, 'session') or conf.getint(section, 'session') != os.getpid():
        log.info('Creating new DXVK config')
        set_environment('DXVK_CONFIG_FILE', cfile)

        conf = configparser.ConfigParser()
        conf.optionxform = str
        conf.set(section, 'session', str(os.getpid()))

        if os.access(dxvk_conf, os.F_OK):
            conf.read_file(read_dxvk_conf(open(dxvk_conf)))
        log.debug(conf.items(section))

    # set option
    log.info('Addinging DXVK option: '+ str(opt) + ' = ' + str(val))
    conf.set(section, opt, str(val))

    with open(cfile, 'w') as configfile:
        conf.write(configfile)
