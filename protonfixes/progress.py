""" Module to track the progress of fixes
"""

from .logger import log


TOTAL_STEPS = 0


class TrackProgressFactory: #pylint: disable=invalid-name
    #pylint: disable=too-few-public-methods
    """ Class that counts the number of functions registered with
        its decorator, and increments splash screen step every time
        a function is called
    """
    registry = []

    def __call__(self, fmt_string):
        def decorator(function):
            registry_entry = '{}.{}'.format(function.__module__,
                                            function.__name__)
            self.registry.append(registry_entry.replace('protonfixes.', ''))
            def wrapper(*args, **kwargs):
                log.info(fmt_string.format(*args, **kwargs))
                return function(*args, **kwargs)
            return wrapper
        return decorator

TrackProgress = TrackProgressFactory() #pylint: disable=invalid-name
