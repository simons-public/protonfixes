#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Game fix for STAR WARS™ Galactic Battlegrounds Saga (356500)
"""
#pylint: disable=C0103

__updated__ = '2022-03-21 23:09:28'

import pathlib as pl

from protonfixes import util


def main():
    """
    * Fix GUI issues by using virtual desktop.
    * Fix multiplayer by installing 'directplay'.
    * Fix startup by not using the launcher.
    """
    # the menu is *always* 800x600 and this setting doesn't affect in game resolution
    # taken from [here](https://www.protondb.com/app/356500#zKoYYDdEIs)
    util.protontricks('settings vd=800x600')

    # to fix multiplayer
    # as of Proton 7.0-1 before 'directplay' can be installed, the existing files need to be removed
    files_to_remove = set([
        'dplaysvr.exe', 'dplayx.dll', 'dpnet.dll', 'dpnhpast.dll',
        'dpnsvr.exe', 'dpwsockx.dll'
    ])
    prefix_path = pl.Path(util.protonprefix())
    lib_path = 'syswow64'
    if util.win32_prefix_exists():
        lib_path = 'system32'

    for file_to_remove in files_to_remove:
        try:
            (prefix_path / 'drive_c' / 'windows' / lib_path /
             file_to_remove).unlink()
        except FileNotFoundError:
            pass
    # as of Proton 7.0-1 the verb 'directplay' must be installed to make LAN multiplayer work
    util.protontricks('directplay')

    # taken from [here](https://www.protondb.com/app/356500#zKoYYDdEIs)
    util.replace_command('player.exe', 'battlegrounds_x1.exe')
