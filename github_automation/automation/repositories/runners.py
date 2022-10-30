from github_automation.api.repositories import PullRequestData
from github_automation.automation.core import Runnable
from github_automation.automation.repositories import execution


class ReposLister(Runnable):
    def __init__(self):
        super().set_context('./github_automation/configuration/context_files/use_case_for_organizations_repos.yaml')

    def execute(self):
        context = super().get_context()
        execution.list_repos(context.organizations, context.repositories)


class PullRequestCreator(Runnable):
    def __init__(self):
        super().set_context('./github_automation/configuration/context_files/use_case_for_multiple_organizations.yaml')

    def execute(self):
        pr = PullRequestData('Testing PR', 'This is a testing PR', 'dev', 'main')
        context = super().get_context()
        execution.create_prs(pr, context.organizations, context.repositories)
