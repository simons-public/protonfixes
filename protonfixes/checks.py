""" Run some tests and generate warnings for proton configuration issues
"""

from .logger import log

def esync_file_limits():
    """
    Check esync file limits using /proc/sys/fs/file-max
    https://www.reddit.com/r/SteamPlay/comments/9kqisk/tip_for_those_using_proton_no_esync1/
    """

    warning = '''File descriptor limit is low
    This can cause issues with ESYNC
    For more details see:
    https://github.com/zfigura/wine/blob/esync/README.esync
    '''

    with open('/proc/sys/fs/file-max') as fsmax:
        max_files = fsmax.readline()
        if int(max_files) < 8192:
            log.warn(warning)


def run_checks():
    """ Run checks to notify of any potential issues
    """

    log.info('Running checks')
    esync_file_limits()
