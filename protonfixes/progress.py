""" Module to track the progress of fixes
"""

import ast
from .logger import log
from . import splash


CURRENT_STEP = 0
TOTAL_STEPS = 0


class TrackProgressFactory: #pylint: disable=invalid-name
    #pylint: disable=too-few-public-methods
    """ Class that counts the number of functions registered with
        its decorator, and increments splash screen step every time
        a function is called
    """

    def __init__(self):
        self.registry = []

    def __call__(self, fmt_string):
        def decorator(function):
            registry_entry = '{}.{}'.format(function.__module__,
                                            function.__name__)
            self.registry.append(registry_entry)
            def wrapper(*args, **kwargs):
                set_progress_text(fmt_string.format(*args, **kwargs))
                res = function(*args, **kwargs)
                increase_progress()
                return res
            return wrapper
        return decorator

TrackProgress = TrackProgressFactory() #pylint: disable=invalid-name


class FunctionCallVisitor(ast.NodeVisitor):
    """ NodeVisitor class that will traverse a python file and
        return a list of fully qualified function calls
    """
    def __init__(self):
        super().__init__()
        self.functioncalls = []
        self.translation = {}

    def visit_Call(self, node): #pylint: disable=invalid-name
        """ Method that visits function calls, translates them
            into a fully qualified call and adds them to functioncalls
        """
        if hasattr(node.func, 'attr'):
            func_call = node.func.attr
        elif hasattr(node.func, 'id'):
            func_call = node.func.id
        else:
            return
        try:
            prefix = node.func.value.id
        except AttributeError:
            prefix = None
        if prefix is not None:
            raw_call = prefix + '.' + func_call
        else:
            raw_call = func_call
        call_components = raw_call.split('.')
        call_prefix = call_components[0]
        if call_prefix in self.translation:
            call_components[0] = self.translation[call_prefix]
        self.functioncalls.append('.'.join(call_components))

    def visit_ImportFrom(self, node): #pylint: disable=invalid-name
        """ Import visitor, will read import nodes and build a translation
            table to allow function calls to be translated into fully qualified
            calls
        """
        mod = node.module
        for name in node.names:
            targetname = mod + '.' + name.name
            if name.asname is None:
                self.translation[name.name] = targetname
            else:
                self.translation[name.asname] = targetname


def parse_fix(path):
    """ Given a python file in path, parse it and count the steps
    """
    global TOTAL_STEPS #pylint: disable=global-statement
    visitor = FunctionCallVisitor()
    with open(path) as fix_file:
        fix_ast = ast.parse(fix_file.read())
        visitor.visit(fix_ast)
    relevant_calls = [x for x in visitor.functioncalls
                      if x in TrackProgress.registry]
    TOTAL_STEPS = len(relevant_calls)


def increase_progress():
    """ Increases CURRENT_STEP and updates the progress bar
    """
    global CURRENT_STEP #pylint: disable=global-statement
    CURRENT_STEP += 1
    splash.set_splash_progress(int(CURRENT_STEP/(TOTAL_STEPS)*100))
    log.debug("Step {}/{}".format(CURRENT_STEP, TOTAL_STEPS))



def set_progress_text(text):
    """ Sets the progress description text
    """
    if len(text) > 50:
        text = text[:50]
        text += '...'
    splash.set_splash_text(text)
