""" Default gamefix for running from Steam launch options
"""

import sys
from protonfixes import util

def main():
    """ global defaults
    """

    # Steam commandline
    def use_steam_commands():
        """ Parse aliases from Steam launch options
        """
        pf_alias_list = list(filter(lambda item: '-pf_' in item, sys.argv))

        for pf_alias in pf_alias_list:
            sys.argv.remove(pf_alias)
            if pf_alias == '-pf_winecfg':
                util.winecfg()
            elif pf_alias == '-pf_regedit':
                util.regedit()
            elif pf_alias.split('=')[0] == '-pf_tricks':
                param = str(pf_alias.replace('-pf_tricks=', ''))
                util.protontricks(param)
            elif pf_alias.split('=')[0] == '-pf_dxvk_set':
                param = str(pf_alias.replace('-pf_dxvk_set=', ''))
                dxvk_opt = param.split('=')
                util.set_dxvk_option(str(dxvk_opt[0]), str(dxvk_opt[1]))

    use_steam_commands()
