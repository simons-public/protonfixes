""" Game engine API
"""

import os
import sys
from .logger import log

class Engine():
    """ Game engines
    """

    def __init__(self):
        self.engine_name = None
        self.supported = {
            'Dunia 2': 'https://pcgamingwiki.com/wiki/Engine:Dunia_2',
            'Unity': 'https://pcgamingwiki.com/wiki/Engine:Unity',
            'RAGE' : 'https://pcgamingwiki.com/wiki/Grand_Theft_Auto_IV#Launch_Options',
            'UE3'  : 'https://pcgamingwiki.com/wiki/Engine:Unreal_Engine_3',
            'UE4'  : 'https://pcgamingwiki.com/wiki/Engine:Unreal_Engine_4'
        }

        # Autodetection
        if self._is_unity():
            self.engine_name = 'Unity'
        elif self._is_rage():
            self.engine_name = 'RAGE'
        elif self._is_ue3():
            self.engine_name = 'UE3'
        elif self._is_ue4():
            self.engine_name = 'UE4'
        elif self._is_dunia2():
            self.engine_name = 'Dunia 2'
            # TODO: dxgi.nvapiHack=False
        else:
            log.info('Engine: unknown Game engine')

        if self.engine_name is not None:
            log.info('Engine: ' + self.engine_name)
            log.info('Engine: ' + self.supported[self.engine_name])


    def _add_argument(self, args=''):
        """ Set command line arguments
        """

        sys.argv += args.split(' ')


    def _is_unity(self):
        """ Detect Unity engine
        """

        dir_list = os.listdir(os.environ['PWD'])
        data_list = list(filter(lambda item: 'Data' in item, dir_list))

        # Check .../Gamename_Data/Mono/etc/ dir
        for data_dir in data_list:
            if os.path.exists(os.path.join(os.environ['PWD'], data_dir, 'Mono/etc')):
                return True

        return False


    def _is_dunia2(self):
        """ Detect Dunia 2 engine (Far Cry >= 3)
        """

        dir_list = os.listdir(os.environ['PWD'])
        data_list = list(filter(lambda item: 'data_win' in item, dir_list))

        # Check .../data_win*/worlds/multicommon dir
        for data_dir in data_list:
            if os.path.exists(os.path.join(os.environ['PWD'], data_dir, 'worlds/multicommon')):
                return True

        return False

    def _is_rage(self):
        """ Detect RAGE engine (GTA IV/V)
        """

#        dir_list = os.listdir(os.environ['PWD'])

#        # Check .../*/pc/data/cdimages dir
#        for data_dir in dir_list:
#            if os.path.exists(os.path.join(os.environ['PWD'], data_dir, 'pc/data/cdimages')):
#                return True
        if os.path.exists(os.path.join(os.environ['PWD'], 'pc/data/cdimages')):
            return True

        return False

    def _is_ue3(self):
        """ Detect Unreal Engine 3
        """

        return False


    def _is_ue4(self):
        """ Detect Unreal Engine 4
        """

        return False


    def _log(self, ctx, msg, warn=False):
        """ Log wrapper
        """

        if self.engine_name is None:
            log.warn(ctx + ': Engine not defined')
        elif warn is not False:
            log.warn(self.engine_name + ': ' + ctx + ': ' + msg)
        else:
            log.info(self.engine_name + ': ' + ctx + ': ' + msg)


    def name(self):
        """ Report Engine name
        """
        return self.engine_name


    def set(self, _engine=None):
        """ Force engine
        """

        if _engine in self.supported:
            self.engine_name = _engine
            self._log('set', 'forced')
        else:
            log.warn('Engine not supported (' + engine + ')')


    def nosplash(self):
        """ Disable splash screen
        """

        if self.engine_name == 'UE3':
            self._add_argument('-nosplash')
            self._log('nosplash', 'splash screen disabled', True)
        else:
            self._log('nosplash', 'not supported', True)


    def info(self):
        """ Show some information about engine
        """

        if self.engine_name == 'RAGE':
            self._add_argument('-help')
            self._log('info', 'command line arguments')
        else:
            self._log('info', 'not supported', True)


    def nointro(self):
        """ Skip intro videos
        """

        if self.engine_name == 'UE3':
            self._add_argument('-nostartupmovies')
            self._log('nointro', 'intro videos disabled')
        elif self.engine_name == 'Dunia 2':
            self._add_argument('-skipintro')
            self._log('nointro', 'intro videos disabled')
        else:
            self._log('nointro', 'not supported', True)


    def launcher(self):
        """ Force launcher
        """

        if self.engine_name == 'Unity':
            self._add_argument('-show-screen-selector')
            self._log('launcher', 'forced')
        else:
            self._log('launcher', 'not supported', True)

    def windowed(self):
        """ Force windowed mode
        """

        if self.engine_name == 'Unity':
            self._add_argument('-popupwindow -screen-fullscreen 0')
            self._log('windowed', 'borderless window')
        elif self.engine_name == 'RAGE':
            self._add_argument('-windowed')
            self._log('windowed', 'window')
        else:
            self._log('windowed', 'not supported', True)


    def resolution(self, res=None):
        """ Force screen resolution
        """

        if res is not None:
            res_wh = res.split('x')

        if self.engine_name == 'Unity':
            self._add_argument('-screen-width ' + res_wh[0] + ' -screen-height ' + res_wh[1])
            self._log('resolution', res)
        elif self.engine_name == 'RAGE':
            self._add_argument('-width ' + res_wh[0] + ' -height ' + res_wh[1])
            self._log('resolution', res)
        else:
            self._log('resolution', 'not supported', True)


engine = Engine() #pylint: disable=C0103
