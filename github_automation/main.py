#!/usr/bin/env python

import sys
from typing import Optional

from termcolor import colored

from github_automation.automation import core
from github_automation.cli import cli
from github_automation.configuration.logger import instance
from github_automation.configuration.config import APP_BANNER

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


def run(arg: str = sys.argv[1]) -> Optional[int]:
    opt = cli.parse_input(arg)
    logger.debug(f'Option {opt.name} selected')
    if opt.value.has_runner:
        core.execute(opt.value.runnable)

    return None


if __name__ == '__main__':
    if APP_BANNER is True:
        print(colored(banner, "green"), file=sys.stderr)
    sys.exit(run())
