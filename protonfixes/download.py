""" Module with helper functions to download from file-hosting providers
"""

import os
import hashlib
import zipfile
import urllib.request
import http.cookiejar
from .progress import TrackProgress
from .logger import log
from . import config


GDRIVE_URL = 'https://drive.google.com/uc?id={}&export=download'
HASH_BLOCK_SIZE = 65536


def get_filename(headers):
    """ Retrieve a filename from a request headers via Content-Disposition
    """
    content_disp = [x for x in headers if x[0] == 'Content-Disposition'][0][1]
    raw_filename = [x for x in content_disp.split(';') if x.startswith('filename=')][0]
    return raw_filename.replace('filename=', '').replace('"', '')


@TrackProgress("Downloading file from gdrive")
def gdrive_download(gdrive_id, path):
    """ Download a file from gdrive given the fileid and a path to save
    """
    url = GDRIVE_URL.format(gdrive_id)
    cjar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
    urllib.request.install_opener(opener)
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    confirm_cookie = [x for x in resp.getheaders() if
                      (x[0] == 'Set-Cookie'
                       and x[1].startswith('download_warning'))][0][1]
    confirm = confirm_cookie.split(';')[0].split('=')[1]
    req2 = urllib.request.Request(url + '&confirm={}'.format(confirm))
    resp2 = urllib.request.urlopen(req2)
    filename = get_filename(resp2.getheaders())
    with open(os.path.join(path, filename), 'wb') as save_file:
        save_file.write(resp2.read())


@TrackProgress("Downloading zip from: {}")
def install_from_zip(url, filename, path=os.getcwd(), filesha=None):
    """ Install a file from a downloaded zip
    """

    if (os.path.isfile(os.path.join(path, filename))
            and filesha is not None
            and sha256sum(filename) == filesha):
        log.info('File ' + filename + ' found in ' + path)
        return

    cache_dir = config.cache_dir
    zip_file_name = os.path.basename(url)
    zip_file_path = os.path.join(cache_dir, zip_file_name)

    if zip_file_name not in os.listdir(cache_dir):
        log.info('Downloading ' + filename + ' to ' + zip_file_path)
        urllib.request.urlretrieve(url, zip_file_path)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_obj:
        log.info('Extracting ' + filename + ' to ' + path)
        zip_obj.extract(filename, path=path)


def sha1sum(filename):
    """ Computes the sha1sum of the specified file
    """
    if not os.path.isfile(filename):
        return ''
    hasher = hashlib.sha1()
    with open(filename, 'rb') as hash_file:
        buf = hash_file.read(HASH_BLOCK_SIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = hash_file.read(HASH_BLOCK_SIZE)
    return hasher.hexdigest()


def sha256sum(filename):
    """ Computes the sha1sum of the specified file
    """
    if not os.path.isfile(filename):
        return ''
    hasher = hashlib.sha256()
    with open(filename, 'rb') as hash_file:
        buf = hash_file.read(HASH_BLOCK_SIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = hash_file.read(HASH_BLOCK_SIZE)
    return hasher.hexdigest()
