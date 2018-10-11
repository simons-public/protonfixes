import os
import sys

class Log():
    """Log to stderr for steam dumps
    """

    def __init__(self):
        self.pfx = 'ProtonFixes[' + str(os.getpid()) + '] '
        self.colors = {
            'RESET': '\u001b[0m',
            'INFO': '\u001b[34m',
            'WARN': '\u001b[33m',
            'CRIT': '\u001b[31m',
            'DEBUG': '\u001b[35m'
        }

    def log(self, msg='', level='INFO'):
        pfx = self.pfx + level + ': '
        color = self.colors[level]
        reset = self.colors['RESET']
        sys.stderr.write(color + pfx + str(msg) + reset + os.linesep)
        sys.stderr.flush()

    def info(self, msg):
        self.log(msg, 'INFO')

    def warn(self, msg):
        self.log(msg, 'WARN')

    def crit(self, msg):
        self.log(msg, 'CRIT')

    def debug(self, msg):
        if 'DEBUG' in os.environ:
            self.log(msg, 'DEBUG')
        

