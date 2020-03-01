""" Game fix for Doom 2016
"""
#pylint: disable=C0103

from protonfixes import util, download

def main():
    """ Install vcrun2015
    """

    # https://github.com/ValveSoftware/Proton/issues/788#issuecomment-416651267
    util.protontricks('vcrun2015')

    # disable chroma implementation that is broken in wine
    # https://github.com/simons-public/protonfixes/issues/26
    chroma_url = 'https://github.com/Riesi/CChromaEditor/files/2277158/CChromaEditorLibrary.zip'
    download.install_from_zip(chroma_url,
                              'CChromaEditorLibrary.dll',
                              util.get_game_install_path(),
                              '0b947580ed2a13dd8c8f0c987d5c7993281e64ab967368ba8d72c8b82e2d906a')
