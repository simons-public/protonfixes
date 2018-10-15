""" Tests for the util.py helpers
"""

import os
import sys
import glob
import time
import shutil
import subprocess
import unittest
from protonfixes import util


class Quiet:
    def __enter__(self):
        self.stdout, self.stderr = sys.stdout, sys.stderr
        self.null = open(os.devnull, 'w')
        sys.stdout = sys.stderr = self.null

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.null.close()
        sys.stdout, sys.stderr = self.stdout, self.stderr

def setup_testenv(gameid):
    """ Setup the test environment variables
    """

    sys.argv[0] = glob.glob(os.path.expanduser('~/.local/share/Steam/steamapps/common/Proton*/proton'))[0]

    test_env = {
        'STEAM_COMPAT_DATA_PATH': '/tmp/protonfixes_test/' + str(gameid),
        'SteamUser': 'steamuser',
        'ENABLE_VK_LAYER_VALVE_steam_overlay_1': '1',
        'WINEDEBUG': '-all',
        }

    test_env['STEAM_COMPAT_CLIENT_INSTALL_PATH'] = os.path.expanduser('~/.local/share/Steam')
    test_env['STEAM_RUNTIME'] = os.path.expanduser('~/.local/share/Steam/ubuntu12_32/steam-runtime')

    os.environ.update(test_env)
    return test_env


def setup_testpfx(gameid):
    """ Create a test prefix
    """

    test_env = setup_testenv(gameid)
    os.environ.update(test_env)
    prefix = test_env['STEAM_COMPAT_DATA_PATH']
    try:
        shutil.rmtree(prefix)
    except FileNotFoundError:
        pass
    os.makedirs(prefix)
    proton_bin = glob.glob(os.path.join(
        test_env['STEAM_COMPAT_CLIENT_INSTALL_PATH'], 'steamapps/common/Proton*/proton'))[0]

    with open(os.devnull, 'w') as devnull:
        subprocess.run(
            [proton_bin, 'getnativepath', 'C:\\windows\\notepad.exe'],
            stdout=devnull, stderr=devnull)

    return prefix


def tearDownModule():
    """ Remove the protonfixes_test dir from /tmp
    """
    try:
        shutil.rmtree('/tmp/protonfixes_test/')
    except OSError:
        time.sleep(1)
        shutil.rmtree('/tmp/protonfixes_test/')

@unittest.skipUnless(os.name == 'posix', 'Not testing on windows')
class TestWhich(unittest.TestCase):
    """ util.py which tests
    """
    def test_return(self):
        """ Should return exactly like shutil.which
        """

        self.assertEqual(shutil.which('hostname'), util.which('hostname'))

    def test_executable(self):
        """ The returned path should be executable
        """

        true_bin = util.which('true')
        return_code = subprocess.call(true_bin, env={})

        self.assertEqual(return_code, 0)


@unittest.skipUnless(os.name == 'posix', 'Not testing on windows')
class TestProtonDir(unittest.TestCase):
    """ util.py protondir tests
    """
    @classmethod
    def setUpClass(cls):
        setup_testenv(1000)

    def test_is_dir(self):
        """ Check if a directory is returned
        """

        proton_dir = util.protondir()
        self.assertTrue(os.path.isdir(proton_dir))

    def test_return(self):
        """ Check if proton files are in directory
        """

        proton_files = os.listdir(util.protondir())
        self.assertTrue('proton' in proton_files)
        self.assertTrue('toolmanifest.vdf' in proton_files)
        self.assertTrue('proton_dist.tar.gz' in proton_files)
        self.assertTrue('version' in proton_files)
        self.assertTrue('dist' in proton_files)

@unittest.skipUnless(os.name == 'posix', 'Not testing on windows')
class TestProtonPrefix(unittest.TestCase):
    """ util.py protonprefix tests
    """

    @classmethod
    def setUpClass(cls):
        setup_testpfx(1001)

    def test_is_dir(self):
        """ Check if a directory is returned
        """

        prefix = util.protonprefix()
        self.assertTrue(os.path.isdir(prefix))

    def test_prefix_valid(self):
        """ Check if prefix contains required files
        """

        prefix_files = os.listdir(util.protonprefix())
        self.assertTrue('dosdevices' in prefix_files)
        self.assertTrue('drive_c' in prefix_files)
        self.assertTrue('userdef.reg' in prefix_files)
        self.assertTrue('user.reg' in prefix_files)


@unittest.skipUnless(os.name == 'posix', 'Not testing on windows')
class TestProtonTricks(unittest.TestCase):
    """ util.py protontricks tests
    """

    @classmethod
    def setUpClass(cls):
        setup_testpfx(1002)

    def test_installs(self):
        """ Check that protrontricks installs a verb
        """

        with Quiet():
            result = util.protontricks('good')
        self.assertTrue(result)

        prefix = os.path.join(os.environ['STEAM_COMPAT_DATA_PATH'], 'pfx')

        with open(os.path.join(prefix, 'winetricks.log')) as log:
            self.assertTrue('good' in log.read())


@unittest.skipUnless(os.name == 'posix', 'Not testing on windows')
class TestCheckInstalled(unittest.TestCase):
    """ util.py checkinstalled tests
    """

    @classmethod
    def setUpClass(cls):
        setup_testenv(1003)
        logdir = os.path.join(os.environ['STEAM_COMPAT_DATA_PATH'], 'pfx')
        os.makedirs(logdir)
        with open(os.path.join(logdir, 'winetricks.log'), 'w') as log:
            log.write('good')

    def test_return_installed(self):
        """ Check True is returned if verb is in winetricks.log
        """

        with Quiet():
            checkinstalled = util.checkinstalled('good')
        self.assertTrue(checkinstalled)

    def test_return_uninstalled(self):
        """ Check False is returned if verb is not in winetricks.log
        """

        with Quiet():
            checkinstalled = util.checkinstalled('bad')
        self.assertFalse(checkinstalled)

    def test_bad_input(self):
        """ Check False is returned if verb is not a string
        """
        with Quiet():
            zero = util.checkinstalled(0)
            mtlist = util.checkinstalled([])

        self.assertFalse(zero)
        self.assertFalse(mtlist)


@unittest.skipUnless(os.name == 'posix', 'Not testing on windows')
class TestMakeWin32Prefix(unittest.TestCase):
    """ util.py make_win32_prefix tests
    """

    @classmethod
    def setUpClass(cls):
        setup_testenv(1004)

    def test_creates_prefix(self):
        """ Check that a valid win32 prefix is created
        """
        with Quiet():
            util.make_win32_prefix()
        prefix_files = os.listdir(os.environ['STEAM_COMPAT_DATA_PATH'] + '_win32/pfx')
        self.assertTrue('dosdevices' in prefix_files)
        self.assertTrue('drive_c' in prefix_files)
        self.assertTrue('userdef.reg' in prefix_files)
        self.assertTrue('user.reg' in prefix_files)
