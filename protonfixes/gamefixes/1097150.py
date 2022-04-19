""" Game fix for Fall Guys
"""
#pylint: disable=C0103
import os
import subprocess

OLDEXE = 'FallGuysEACLauncher.exe'
NEWEXE = 'FallGuys_client_game.exe'

def main():
    """ Create symlink of eac so at the right location
    """
    if os.path.exists('FallGuys_client_game_Data/Plugins/x86_64/easyanticheat_x64.so'):
        subprocess.call([
            'rm',
            '-rf',
            'FallGuys_client_game_Data/Plugins/x86_64/easyanticheat_x64.so'])
    subprocess.call([
        'ln',
        '-s',
        '../../../EasyAntiCheat/easyanticheat_x64.so',
        'FallGuys_client_game_Data/Plugins/x86_64/easyanticheat_x64.so'])

    # Fixes the ini file.
    subprocess.call([
        'sed',
        '-i',
        f's/TargetApplicationPath={OLDEXE}/TargetApplicationPath={NEWEXE}/',
        'FallGuys_client.ini'])
