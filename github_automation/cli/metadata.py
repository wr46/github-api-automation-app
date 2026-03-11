from github_automation.automation.core import Runnable
from github_automation.cli.flag import Flag


class Metadata:
    def __init__(self, flag: Flag = None, runnable: Runnable = None):
        self.runnable = runnable
        self.flag = flag
        self.has_flag = (flag is not None)
        self.has_runner = (runnable is not None)
