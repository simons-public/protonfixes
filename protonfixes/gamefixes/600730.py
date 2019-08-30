""" Game fix for Trackmania2 Lagoon Demo
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes.logger import log
import os

mania_planet_games = [600720,264850,228760,243360,232910,264660,600730,233070]

def main():
    """ Create a ManiaPlanet folder in comptdata and link every game_bottle to it so that you have one ManiaPlanet instant with all games. No matter what game you launched. (Same as in windows now) 
    """

    game_proton_bottle =  os.path.dirname( os.path.dirname(util.protonprefix()) )
    compdata_folder = os.path.dirname( game_proton_bottle )
    mania_planet_folder = os.path.join( compdata_folder ,"ManiaPlanet")

    if not os.path.exists( mania_planet_folder ):
        log( "Could not find ManiaPlanet directory." )
        log( "Creating new folder and symlinking Games to it." )
        os.rename( game_proton_bottle , mania_planet_folder )
        os.symlink( mania_planet_folder, game_proton_bottle)

        for game_id in mania_planet_games:
            game_path = os.path.join( compdata_folder, str(game_id) )
            if game_path == game_proton_bottle:
                continue
            if os.path.exists( game_path ):
                os.remove( game_id )

            os.symlink( mania_planet_folder, game_path )
        log( "All DONE" )
