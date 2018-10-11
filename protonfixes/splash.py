""" Splash screen for protonfixes using cefpython
"""
import sys
from os import path
from time import sleep
from multiprocessing import Process
from contextlib import contextmanager
from cefpython3 import cefpython as cef
from .logger import Log
log = Log()
# pylint: disable=I1101

def browser(url):
    """ Starts a cef browser in the middle of the screen with url
    """

    # Keeps the splash from displaying on short tasks
    log.info('Delaying splash for 2 seconds')
    sleep(2)
    log.debug('Starting splash screen')

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

    cef.Initialize(settings, switches)

    win_info = cef.WindowInfo()
    win_info.SetAsChild(0, coordinates(600, 360))

    cef.CreateBrowser(url=url, window_info=win_info, window_title='splash')
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

@contextmanager
def splash(page='index.html'):
    """ Runs the browser in a seperate process until the context is returned
    """

    data_dir = path.join(path.dirname(__file__), '..', 'static')
    url = 'file://' + path.join(data_dir, page)
    splashwin = Process(target=browser, args=(url,))
    splashwin.start()
    yield
    log.debug('Terminating splash screen')
    splashwin.terminate()

def _test():
    """ Used for testing the splash with python -m splash
    """

    import time
    with splash():
        while True:
            time.sleep(1)

if __name__ == '__main__':
    _test()
