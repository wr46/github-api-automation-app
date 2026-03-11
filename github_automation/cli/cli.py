import logging
import sys
from enum import Enum

from github_automation.automation.repositories import runners
from github_automation.cli.flag import Flag
from github_automation.cli.metadata import Metadata


class Option(Enum):
    HELP = Metadata(Flag('--help', 'Show options'))
    CMD_LIST_REPOS = Metadata(Flag('--list-repos', 'List Github repositories'), runners.ReposLister())
    CMD_LIST_OPEN_PRS = Metadata(Flag('--list-open-prs', 'List Github user open PRs'), runners.OpenPRsLister())
    CMD_CREATE_PR_REPOS_HV = Metadata(Flag('--create-pr-repos-having', 'Create PR in repositories having'), runners.PullRequestCreator())
    CMD_CREATE_PR_BY_CONTEXT = Metadata(Flag('--create-pr-by-context', 'Create PR in repositories having'), runners.PullRequestCtxCreator())
    CMD_NEW_FEATURE = Metadata(Flag('--new-feat', 'Create PR in repositories having'), runners.NewFeature())
    UNKNOWN = Metadata()


def parse_input(arg: str) -> Option:
    if Option.HELP.value.flag.name == arg:
        show_help()
        return Option.HELP

    return get_option(arg)


def get_option(arg: str) -> Option:
    for opt in list(Option):
        if opt.value.has_flag and opt.value.flag.name == arg:
            return opt

    logging.error(f' Unknown option {arg}, use \'{Option.HELP.value.flag.name}\' for help')
    return Option.UNKNOWN


def show_help():
    print(' How to run it:\n command [OPTION]\n\n Options:', file=sys.stderr)
    for opt in list(Option):
        if opt.value.has_flag:
            print(f' {opt.value.flag.name} : {opt.value.flag.description}', file=sys.stderr)
