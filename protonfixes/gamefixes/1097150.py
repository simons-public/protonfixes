""" Game fix for Fall Guys
"""
#pylint: disable=C0103
import os
import subprocess

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
        's/TargetApplicationPath=FallGuysEACLauncher.exe/TargetApplicationPath=FallGuys_client_game.exe/',
        'FallGuys_client.ini'])
