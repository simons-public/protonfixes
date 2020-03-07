""" Splash screen for protonfixes using cefpython
"""
import os
import sys
import time
import subprocess
import threading
from multiprocessing import Process, Queue
from contextlib import contextmanager
from .logger import log
from . import config

try:
    from cefpython3 import cefpython as cef
    HAS_CEF = True
except ImportError:
    HAS_CEF = False
    log.warn('Optional dependency cefpython3 not found')


STATUS = {}
STATUS['cef_queue'] = Queue()


def control_browser(cef_handle, queue):
    """ Loop thread to send javascript calls to cef
    """
    while not cef_handle.HasDocument():
        time.sleep(2)
    cef_handle.ExecuteFunction('window.setWidth', 0)
    while True:
        operation = queue.get()
        cef_handle.ExecuteFunction(operation[0], operation[1])


#pylint: disable=W0621
def browser(cef, url, cef_queue):
    """ Starts a cef browser in the middle of the screen with url
    """

    # Keeps the splash from displaying on short tasks
    log.debug('Delaying splash for 2 seconds')
    time.sleep(2)
    log.info('Starting splash screen for long-running task')

    settings = {
        'background_color': 0xff000000,
        'cache_path': '',
        'context_menu': {'enabled': False},
        'debug': False,
        'command_line_args_disabled': False,
    }
    switches = {
        'disable-gpu': '',
        'disable-gpu-compositing': '',
    }

    sys.excepthook = cef.ExceptHook
    cef.Initialize(settings, switches)

    win_info = cef.WindowInfo()
    win_info.SetAsChild(0, coordinates(600, 360))
    brow = cef.CreateBrowserSync(url=url, window_info=win_info, window_title='splash')

    control_t = threading.Thread(target=control_browser, args=(brow, cef_queue))
    control_t.start()
    cef.MessageLoop()
    cef.Shutdown()


def coordinates(width, height):
    """ Returns coordinates [x1, y1, x2, y2] for a centered box of width, height
    """

    with open('/sys/class/graphics/fb0/virtual_size', 'r') as res:
        screenx, screeny = map(int, res.read().strip('\n').split(','))

    posx = (screenx/2) - (width/2)
    posy = (screeny/2) - (height/2)

    return [posx, posy, posx+width, posy+height]


def sys_zenity_path():
    """ Returns the path of zenity if found in system $PATH
    """

    steampath = os.environ['PATH'].split(':')
    syspath = [x for x in steampath if 'steam-runtime' not in x]
    for path in syspath:
        zenity_path = os.path.join(path, 'zenity')
        if os.path.exists(zenity_path) and os.access(zenity_path, os.X_OK):
            return zenity_path
    return False


def sys_kdialog_path():
    """ Returns the path of kdialog if found in system $PATH
    """

    steampath = os.environ['PATH'].split(':')
    syspath = [x for x in steampath if 'steam-runtime' not in x]
    for path in syspath:
        kdialog_path = os.path.join(path, 'kdialog')
        if os.path.exists(kdialog_path) and os.access(kdialog_path, os.X_OK):
            return kdialog_path
    return False


@contextmanager
def zenity_splash():
    """ Runs the zenity process until context is returned
    """

    log.debug('Starting zenity splash screen')

    zenity_bin = sys_zenity_path()
    if not zenity_bin:
        return

    zenity_cmd = ' '.join([
        'sleep 2;',
        zenity_bin,
        '--progress',
        '--percentage=0',
        '--no-cancel',
        '--auto-close',
        '--text',
        '"ProtonFixes is running a task, please wait..."',
        ])

    # it would be better to use multiprocessing and time.sleep(2) here,
    # but zenity forks and won't quit when the subprocess is killed,
    # hence, using shell=True and 'sleep 2;'
    zenity = subprocess.Popen(zenity_cmd,
                              encoding='utf-8',
                              stdin=subprocess.PIPE,
                              stdout=None,
                              stderr=None,
                              shell=True,
                             )
    STATUS['zenity_handle'] = zenity
    yield
    log.debug('Terminating zenity splash screen')
    zenity.stdin.write('100\n')
    zenity.stdin.flush()


@contextmanager
def kdialog_splash():
    """ Runs the kdialog process until context is returned
    """

    log.debug('Starting kdialog splash screen')

    kdialog_bin = sys_kdialog_path()
    if not kdialog_bin:
        return

    kdialog_cmd = [
        kdialog_bin,
        '--progressbar',
        '"ProtonFixes is running a task, please wait..."',
        '100'
        ]

    out = subprocess.check_output(kdialog_cmd)
    kdialog = ['qdbus'] + out.decode().strip('\n').split(' ')
    subprocess.call(kdialog + ['showCancelButton', 'false'])
    STATUS['kdialog_handle'] = kdialog
    yield
    log.debug('Terminating kdialog splash screen')
    subprocess.call(kdialog + ['Set', '', 'value', '100'])
    subprocess.call(kdialog + ['close'])


@contextmanager
#pylint: disable=W0621
def cef_splash(cef, page='index.html'):
    """ Runs the browser process until the context is returned
    """

    log.debug('Starting CEF splash screen')
    data_dir = os.path.join(os.path.dirname(__file__), 'static')
    url = 'file://' + os.path.join(data_dir, page)
    cef_proc = Process(target=browser, args=(cef, url, STATUS['cef_queue']))
    cef_proc.start()
    try:
        yield
    finally:
        cef_proc.terminate()
        sys.excepthook = sys.__excepthook__
    log.debug('Terminating CEF splash screen')
    cef_proc.terminate()


@contextmanager
def splash():
    """ Wrapper logic to choose the zenity or cef splash screen
    """

    log.debug('Starting splash screen')

    is_bigpicture = 'SteamTenfoot' in os.environ

    if not config.enable_splash:
        yield
        return

    for splash in config.splash_preference.split(','):
        if splash.strip() == 'cef' and HAS_CEF:
            log.debug('Using cefpython splash screen')
            with cef_splash(cef):
                STATUS['handler'] = 'cef'
                yield
                return

        if (splash.strip() == 'kdialog' and sys_kdialog_path()
                and (not is_bigpicture or config.kdialog_bigpicture)):
            log.debug('Using kdialog splash screen')
            with kdialog_splash():
                STATUS['handler'] = 'kdialog'
                yield
                return

        if (splash.strip() == 'zenity' and sys_zenity_path()
                and (not is_bigpicture or config.zenity_bigpicture)):
            log.debug('Using zenity splash screen')
            with zenity_splash():
                STATUS['handler'] = 'zenity'
                yield
                return

    log.warn('No splash dependencies found, running without splash screen')
    yield
    return


def set_splash_text(text):
    """ Set splash screen text
    """
    if STATUS['handler'] == 'kdialog':
        kdialog = STATUS['kdialog_handle']
        subprocess.call(kdialog + ['setLabelText', text])
    elif STATUS['handler'] == 'zenity':
        zenity = STATUS['zenity_handle']
        zenity.stdin.write('#' + text + '\n')
        zenity.stdin.flush()
    elif STATUS['handler'] == 'cef':
        cef_q = STATUS['cef_queue']
        cef_q.put(('setText', text))
    else:
        log.info(text)


def set_splash_progress(progress):
    """ Set splash screen progress in a 0-100 scale
    """
    if STATUS['handler'] == 'kdialog':
        kdialog = STATUS['kdialog_handle']
        subprocess.call(kdialog + ['Set', '', 'value', str(progress)])
    elif STATUS['handler'] == 'zenity':
        zenity = STATUS['zenity_handle']
        zenity.stdin.write(str(progress) + '\n')
        zenity.stdin.flush()
    elif STATUS['handler'] == 'cef':
        cef_q = STATUS['cef_queue']
        cef_q.put(('setWidth', progress))
    else:
        log.info("Progress {}%".format(progress))
