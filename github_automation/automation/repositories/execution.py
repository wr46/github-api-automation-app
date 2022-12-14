from typing import List

from github import Repository, AuthenticatedUser

from github_automation.api import users, organizations, repositories
from github_automation.configuration.logger import instance

logger = instance.get_logger()


def list_repos(orgs: List[str], repos: List[str]):
    orgs: List[str] = organizations.get_organizations(orgs)
    for repo in repositories.get_repositories(repos, orgs, users.get_user()):
        print(repo.name)


def create_prs(pr: repositories.PullRequestData, orgs: List[str], repos: List[str]):
    print(orgs)
    print(repos)
    # if len(orgs) > 0:
    #    create_prs_by_organizations(pr, orgs, repos)
    # else:
    #    create_prs_by_user(pr, users.get_user(), repos)


def create_prs_by_organizations(pr: repositories.PullRequestData, orgs: List[str], repos: List[str]):
    repos_len: int = len(repos)
    for org_name in orgs:
        org = organizations.get_organization(org_name)
        for repo in repositories.get_org_repositories(org):
            if repos_len == 0 or repo.name in repos:
                repositories.create_pull_request(pr, repo)


def create_prs_by_user(pr: repositories.PullRequestData, user: AuthenticatedUser, repos_names: List[str]):
    repos: [Repository]
    if len(repos_names) == 0:
        repos = repositories.get_user_repositories(user)
    else:
        repos = repositories.get_user_repositories_by_name(user, repos_names)

    for repo in repos:
        repositories.create_pull_request(pr, repo)
