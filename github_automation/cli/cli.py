import logging
import sys
from enum import Enum


class Option(Enum):
    HELP = '--help'
    CMD_LIST_REPOS = '--list-repos'
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
    print(f'{Option.HELP} : Show options', file=sys.stderr)
    print(f'{Option.CMD_LIST_REPOS} : List Github repositories', file=sys.stderr)
