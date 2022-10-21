#!/usr/bin/env python

import logging
import sys
from typing import Optional
from termcolor import colored

from github_automation.cli import cli
from github_automation.cli.cli import Option
from github_automation.configuration import config

LOG_FORMAT = '%(asctime)s [%(levelname)s] %(message)s'
logging.basicConfig(format=LOG_FORMAT, datefmt='%d/%m/%Y %H:%M:%S', level=config.LOG_LEVEL)

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

    if Option.CMD_TEST == opt:
        print('Hello World!')

    return None


if __name__ == '__main__':
    sys.exit(run())
