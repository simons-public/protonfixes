""" Game fix for Metal Slug 3
"""
# pylint: disable=C0103
import hashlib
import io
import os.path
import urllib.request
import zipfile

from protonfixes.logger import log
from protonfixes import util

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

    log('Applying fixes for Metal Slug 3')
    metal_slug_path = util.get_game_install_path()

    # download new DLL files and replace existing ones
    for dll in REPLACEMENT_DLLS:
        # check if current dlls are already the replacements
        cur_dll_path = os.path.join(metal_slug_path, dll)
        cur_sha = hashlib.sha256()

        try:
            with open(cur_dll_path, 'rb') as cur_dll_data:
                cur_sha.update(cur_dll_data.read())

            if cur_sha.hexdigest() == REPLACEMENT_DLLS[dll]['sha256']:
                log(f"{dll} is already the replacement dll. Skipping replacing it...")
                continue
        except FileNotFoundError:
            log(f"{dll} not found, will use the one from the zip.")

        req = urllib.request.urlopen(REPLACEMENT_DLLS[dll]['url'])
        # check http return code and if not 200 log and skip file
        if req.getcode() != 200:
            log(f"Received HTTP {req.status} when downloading replacement DLL {dll} skipping...")
            continue

        dll_zip = zipfile.ZipFile(io.BytesIO(req.read()))
        dll_data = dll_zip.open(dll.lower())

        sha = hashlib.sha256()
        sha.update(dll_data.read())

        if sha.hexdigest() != REPLACEMENT_DLLS[dll]['sha256']:
            log(f"DLL SHA256 does not match for {dll} skipping...")
            continue

        dll_data = dll_zip.open(dll.lower())
        with open(cur_dll_path, 'wb') as out_dll:
            log(f"Writing replacement DLL data to {cur_dll_path}")
            out_dll.write(dll_data.read())
