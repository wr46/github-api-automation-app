from github_automation.api.repositories import PullRequestData
from github_automation.automation.core import Runnable
from github_automation.automation.repositories import execution


class ReposLister(Runnable):
    def execute(self):
        execution.list_repos()


class PullRequestCreator(Runnable):
    def execute(self):
        pr = PullRequestData('Testing PR', 'This is a testing PR', 'dev', 'main')
        execution.create_prs(pr, [], [])
