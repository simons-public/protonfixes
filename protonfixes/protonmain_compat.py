""" Compatibility shim to support Proton versions lower than 4.11-2
"""
#pylint: disable=R0903,R1705

import os
from .protonversion import semver_cmp, PROTON_VERSION

OLD_PROTON = "4.11-1"


PROTON_MAP = {'base_dir': 'basedir',
              'bin_dir': 'bindir',
              'lib_dir': 'libdir',
              'lib64_dir': 'lib64dir',
              'fonts_dir': 'fontsdir',
              'wine_bin': 'wine_path',
              'prefix_dir': 'prefix'}


class Proxy():
    #pylint: disable=C0115
    def __init__(self, proxy_object, remap_dict=None):
        self._proxy_object = proxy_object
        self._remap_dict = remap_dict or {}

    def __getattribute__(self, name):
        if name.startswith('_'):
            return object.__getattribute__(self, name)
        else:
            if name in self._remap_dict:
                name = self._remap_dict[name]
            return getattr(self._proxy_object, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            return object.__setattr__(self, name, value)
        else:
            if name in self._remap_dict:
                name = self._remap_dict[name]
            return setattr(self._proxy_object, name, value)


class DummyClass():
    #pylint: disable=C0115
    def __init__(self):
        pass


class ProtonCompat():
    #pylint: disable=C0115
    def __init__(self, proton):
        self.g_proton = Proxy(proton, PROTON_MAP)
        self.g_proton.wineserver_bin = os.path.join(self.g_proton.bindir, 'wineserver')
        self.g_session = DummyClass()
        self.g_session.env = proton.env
        self.g_session.dlloverrides = proton.dlloverrides
        self.g_compatdata = self.g_proton


if not semver_cmp(OLD_PROTON, PROTON_VERSION):
    import __main__ as protonmain #pylint: disable=W0611
else:
    import __main__ as old_protonmain
    protonmain = ProtonCompat(old_protonmain) #pylint: disable=C0103
