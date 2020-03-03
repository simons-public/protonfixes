""" Game fix for Metal Slug
"""
# pylint: disable=C0103
from protonfixes import util, download
from protonfixes.logger import log


REPLACEMENT_DLLS = {
    'd3dcompiler_46.dll': {
        'sha256': '58d9a00888af693b2a5222fe74cfded32ce83e74f85b474f1cbe5987217b5a9d',
        'url': 'https://github.com/alanjjenkins/proton-dlls/raw/master/d3dcompiler_46.zip'
    },
    'libEGL.dll': {
        'sha256': 'd38bcbf0ebbd44b83d1d0ebc7b2fe6dceb08292282fccc473df58d452429ec84',
        'url': 'https://github.com/alanjjenkins/proton-dlls/raw/master/libegl.zip'
    },
    'libGLESv2.dll': {
        'sha256': '9bdfde3e90cc7c6d5360ac1cb31a6a6a64872d9e6a8a880584146dc452196a23',
        'url': 'https://github.com/alanjjenkins/proton-dlls/raw/master/libglesv2.zip'
    }
}


def main():
    """
    Replaces DLL files due to the versions bundled resulting
    in just errors and black screens.
    """

    log('Applying fixes for Metal Slug')
    metal_slug_path = util.get_game_install_path()

    # download new DLL files and replace existing ones
    for dll, props in REPLACEMENT_DLLS.items():
        download.install_from_zip(props['url'],
                                  dll,
                                  metal_slug_path,
                                  props['sha256'])
