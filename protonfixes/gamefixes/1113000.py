""" Game fix for Persona 4 Golden
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ installs devenum, quartz, wmp9, lavfilters and adjust pulse latency
    """

    # Fix pre-rendered cutscene playback
    util.protontricks('devenum')
    util.protontricks('quartz')
    util.protontricks('wmp9')
    util.protontricks('lavfilters')

    # Fix crackling audio
    util.set_environment('PULSE_LATENCY_MSEC', '60')
