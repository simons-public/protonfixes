""" Game fix for Potatoman Seeks the Troof
"""
#pylint: disable=C0103

import os
from protonfixes import util

def main():
    """ The file mms.cfg must have the string OverrideGPUValidation=1 written
    """
    fix_installed = False
    prefix = util.protonprefix()
    macro_path = 'drive_c/windows/syswow64/Macromed/Flash'
    flash_path = os.path.join(prefix, macro_path)
    mms_path = os.path.join(flash_path, 'mms.cfg')
    os.makedirs(flash_path, exist_ok=True)
    if os.path.isfile(mms_path):
        with open(mms_path) as f:
            for line in f:
                if 'OverrideGPUValidation' in line:
                    fix_installed = True
    if not fix_installed:
        with open(mms_path, 'a') as f:
            f.write('\n')
            f.write("OverrideGPUValidation=1")
