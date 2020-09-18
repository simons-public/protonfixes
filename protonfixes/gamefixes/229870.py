""" Game fix for ShootMania Storm
"""
#pylint: disable=C0103

import os
import shutil
from protonfixes import util
from protonfixes.logger import log

mania_planet_games = [228760, 229870, 232910, 233050, 233070,
                      243360, 264660, 264850, 600720, 600730]


def main():
    """ Create a ManiaPlanet folder in compatdata and link the prefixes for every game_bottle.
        With this games ManiaPlanet games can be switched while in game. (Same as in windows now)
    """

    game_proton_bottle = os.path.dirname(os.path.dirname(util.protonprefix()))
    compdata_folder = os.path.dirname(game_proton_bottle)
    mania_planet_pfx = os.path.join(compdata_folder, "ManiaPlanet")

    if not os.path.exists(mania_planet_pfx):
        log("Could not find ManiaPlanet directory.")
        log("Creating new folder and symlinking games to it.")
        pfx_folder = os.path.join(game_proton_bottle, "pfx")
        os.rename(pfx_folder, mania_planet_pfx)
        os.symlink(mania_planet_pfx, pfx_folder)

    for game_id in mania_planet_games:
        game_pfx = os.path.join(compdata_folder, str(game_id), "pfx")
        log("Checking {}".format(game_id))
        if not os.path.exists(game_pfx):
            log("No prefix for {} found, skipping.".format(game_id))
            continue
        if os.path.islink(game_pfx):
            log("{} is already a symlink, skipping.".format(game_id))
            continue

        log("Copying contents of {} to ManiaPlanet folder.".format(game_id))
        for src_dir, _, files in os.walk(game_pfx):
            dst_dir = src_dir.replace(game_pfx, mania_planet_pfx, 1)
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file) or not os.path.exists(src_file):
                    continue
                try:
                    shutil.move(src_file, dst_file)
                    log("Moving {} to {}".format(src_file, dst_file))
                except FileNotFoundError:
                    # FIXME: paths with special chars (&, whitespace) do not work!
                    log("Can't move {}. Continuing anyway.".format(src_file))
        log("Removing {}".format(game_pfx))
        shutil.rmtree(game_pfx)
        log("Symlinking {} prefix to ManiaPlanet folder.".format(game_id))
        os.symlink(mania_planet_pfx, game_pfx)
    log("All DONE")
