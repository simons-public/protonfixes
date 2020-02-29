""" Module for dealing with proton version
"""

import os
import re
import sys
from .logger import log
try:
    from __main__ import CURRENT_PREFIX_VERSION
except ImportError:
    log.warn('Unable to hook into Proton main script environment')
    _PATH_VERSION = re.search(r'Proton (\d*\.\d*)', sys.argv[0])
    if _PATH_VERSION:
        CURRENT_PREFIX_VERSION = _PATH_VERSION.group(1)

VERSION_RE = re.compile(r'(|proton-)(?P<major>\d+)\.(?P<minor>\d+)'+
                        r'(|-(?P<flavor>.*?))-(?P<release>\d+)')


def semver_cmp(ver_1, ver_2):
    """ Compares 2 semver tuples, return True if ver_1 > ver_2, False otherwise
    """
    if isinstance(ver_1, str):
        ver_1 = parse_protonversion(ver_1)
    if isinstance(ver_1, dict):
        ver_1 = version_dicttotuple(ver_1)
    if isinstance(ver_2, str):
        ver_2 = parse_protonversion(ver_2)
    if isinstance(ver_2, dict):
        ver_2 = version_dicttotuple(ver_2)
    for i in range(0, min(len(ver_1), len(ver_2))):
        if ver_1[i] > ver_2[i]: #pylint: disable=no-else-return
            return True
        elif ver_1[i] < ver_2[i]:
            return False
    return False


def parse_protonversion(version_string):
    """ Given a proton version string, return a dict with
        'major', 'minor', 'release' and 'flavor' (eg. GE) if present
    """
    version_re = VERSION_RE.match(version_string)
    if version_re:
        return version_re.groupdict()
    return {}


def version_dicttotuple(dict_version):
    """ Converts a version dictionary into a tuple
    """
    return (int(dict_version['major']),
            int(dict_version['minor']),
            int(dict_version['release']))


def DeprecatedSince(version): #pylint: disable=invalid-name
    """ Decorator to indicate that a fix should only be applied to
        versions older than version
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            if isinstance(version, int):
                if version > PROTON_TIMESTAMP:
                    return function(*args, **kwargs)
            elif isinstance(version, str):
                if semver_cmp(version, PROTON_VERSION):
                    return function(*args, **kwargs)
            return None
        return wrapper
    return decorator


def init():
    """ Initialization function that will create PROTON_VERSION and
        PROTON_TIMESTAMP from the version file
    """
    proton_version = parse_protonversion(CURRENT_PREFIX_VERSION)
    proton_timestamp = 0
    proton_path = os.path.dirname(sys.argv[0])
    proton_version_file = os.path.join(proton_path, 'version')
    try:
        with open(proton_version_file) as version_f:
            version_str = version_f.readline().strip()
            version_components = version_str.split(' ', 2)
            proton_timestamp = int(version_components[0])
            if len(version_components) == 2:
                proton_version = parse_protonversion(version_components[1])
    except OSError:
        log.warn('Proton version file not found in: ' + proton_path)
    return (proton_version, proton_timestamp)


PROTON_VERSION, PROTON_TIMESTAMP = init()
