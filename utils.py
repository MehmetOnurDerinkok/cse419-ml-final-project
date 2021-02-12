import platform

from termcolor import colored as termcolored


IS_WINDOWS = platform.system() == 'Windows'


def colored(value, color='white'):
    if IS_WINDOWS:
        return value
    else:
        return termcolored(value, color)
