import logging
import sys
from enum import Enum


class Option(Enum):
    HELP = '--help'
    CMD_LIST_REPOS = '--list-repos'
    CMD_CREATE_PR_REPOS_HV = '--create-pr-repos-having'
    UNKNOWN = 'unknown'


def parse_input(arg: str) -> Option:
    if Option.HELP.value == arg:
        show_help()
        return Option.HELP

    return get_command(arg)


def get_command(arg: str) -> Option:
    try:
        return Option(arg)
    except ValueError:
        logging.error(f' Unknown option {arg}, use \'{Option.HELP.value}\' for help')
        return Option.UNKNOWN


def show_help():
    print(' How to run it:\n command [OPTION]\n\n Options:', file=sys.stderr)
    print(f' {Option.HELP.value} : Show options', file=sys.stderr)
    print(f' {Option.CMD_LIST_REPOS.value} : List Github repositories', file=sys.stderr)
    print(f' {Option.CMD_CREATE_PR_REPOS_HV.value} : Create PR in repositories having', file=sys.stderr)
