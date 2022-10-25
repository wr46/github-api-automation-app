from github.Repository import Repository

from github_automation.api.repositories import create_pull_request, PullRequestData
from github_automation.automation.main import Runnable
from github_automation.automation.repositories.execution import list_repos


class ReposLister(Runnable):
    def execute(self):
        list_repos()


class PullRequestCreator(Runnable):
    def execute(self):
        pr = PullRequestData()
        repository = Repository()
        create_pull_request(pr, repository)
