#!/usr/bin/env python

import sys
from typing import Optional

from termcolor import colored

from github_automation.automation import core
from github_automation.automation.repositories import runners
from github_automation.cli import cli
from github_automation.cli.cli import Option
from github_automation.configuration.logger import instance

logger = instance.get_logger()

banner = r"""
                                                                                      
  ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗                                        
 ██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗                                       
 ██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝                                       
 ██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗                                       
 ╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝                                       
  ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝                                        
                                                                                      
  █████╗ ██╗   ██╗████████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
 ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
 ███████║██║   ██║   ██║   ██║   ██║██╔████╔██║███████║   ██║   ██║██║   ██║██╔██╗ ██║
 ██╔══██║██║   ██║   ██║   ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
 ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
 ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                      
"""
print(colored(banner, "green"), file=sys.stderr)


def run(arg: str = sys.argv[1]) -> Optional[int]:
    opt = cli.parse_input(arg)
    logger.debug(f'Option {opt.value} selected')

    if Option.CMD_LIST_REPOS == opt:
        core.execute(runners.ReposLister())

    if Option.CMD_CREATE_PR_REPOS_HV == opt:
        core.execute(runners.PullRequestCreator())

    return None


if __name__ == '__main__':
    sys.exit(run())
