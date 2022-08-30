""" Fix for Littlewitch Romanesque: Editio Regia (349300)
"""

from protonfixes import util

def main():
	""" Run the game from S: avoids some file reading issues.
	(The game deletes dots from filepath reading, which usually It's a issue in a SteamLinux standard directory)
	https://github.com/ValveSoftware/Proton/issues/5975#issuecomment-1178969055
	"""
	util.set_environment('PROTON_SET_GAME_DRIVE','1')
