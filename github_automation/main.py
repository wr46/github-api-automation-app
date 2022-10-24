#!/usr/bin/env python

import sys
from typing import Optional

from termcolor import colored

from github_automation.automation.main import execute, list_repos
from github_automation.cli import cli
from github_automation.cli.cli import Option
from github_automation.configuration.logger import get_logger

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
logger = get_logger()


def run(arg: str = sys.argv[1]) -> Optional[int]:
    opt = cli.parse_input(arg)

    if Option.CMD_LIST_REPOS == opt:
        logger.debug(f'Option {Option.CMD_LIST_REPOS.value} selected')
        execute(list_repos)

    return None


if __name__ == '__main__':
    sys.exit(run())
