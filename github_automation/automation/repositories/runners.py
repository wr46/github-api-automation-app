from github_automation.automation.core import Runnable
from github_automation.automation.repositories import execution
from github_automation.automation.repositories.models import PullRequest


class ReposLister(Runnable):
    def __init__(self):
        super().__init__('list_repositories.yaml')

    def execute(self):
        context = super().context()
        execution.list_repos(context.organizations, context.repositories)


class OpenPRsLister(Runnable):
    def __init__(self):
        super().__init__('list_user_prs_by_organizations.yaml')

    def execute(self):
        context = super().context()
        for org in context.organizations:
            execution.list_user_open_prs(org)


class PullRequestCreator(Runnable):
    def __init__(self):
        super().__init__('use_case_for_multiple_organizations.yaml')

    def execute(self):
        context = super().context()
        prs: [PullRequest] = []
        for org in context.organizations:
            for repo in context.repositories:
                pr = PullRequest(repo, 'Testing PR', 'This is a testing PR', 'dev')
                pr.set_organization(org)
                prs.append(pr)
        execution.create_prs(prs)


def pr_template(repo):
    return """
        HERE GOES YOU PR TEMPLATE
    """


class PullRequestCtxCreator(Runnable):
    def __init__(self):
        super().__init__('create_prs_for_filtered_repos_branches.yaml')

    def execute(self):
        context = super().context()
        prs: [PullRequest] = []
        for org in context.organizations:
            for repo in context.repositories:
                pr = PullRequest(repo, 'ci: remove github actions tests', pr_template(repo), 'migrate-github-actions-jenkins')
                pr.set_organization(org)
                prs.append(pr)

        execution.create_prs(prs)


class NewFeature(Runnable):
    def __init__(self):
        super().__init__('new_feature.yaml')

    def execute(self):
        context = super().context()
        for repo in context.repositories:
            execution.testing(repo)

