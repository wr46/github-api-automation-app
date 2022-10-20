import logging
import sys
from enum import Enum


class Option(Enum):
    HELP = '--help'
    CMD_TEST = '--test'
    UNKNOWN = ''


def parse_input(arg: str) -> Option:
    if Option.HELP.value == arg:
        show_help()
        return Option.HELP

    return get_command(arg)


def get_command(arg: str) -> Option:
    try:
        return Option(arg)
    except ValueError:
        logging.error(f'Unknown option {arg}, use \'{Option.HELP.value}\' for help')
        return Option.UNKNOWN


def show_help():
    print('How to run it:\n command [OPTION]\n\nOptions:', file=sys.stderr)
    print('--help : Show options', file=sys.stderr)
    print('--test : Option to echo Hello World', file=sys.stderr)
