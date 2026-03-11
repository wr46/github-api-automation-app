from typing import List

from github import Organization, AuthenticatedUser
from github.GithubException import GithubException
from github_automation.api.auth import api
from github_automation.configuration.logger import instance

logger = instance.get_logger()


def get_organization(organization: str) -> Organization:
    try:
        return api.get_organization(organization)
    except GithubException:
        logger.error(f'Organization with name "{organization}" not found')
        return None


def get_organizations(organizations: List[str]) -> [Organization]:
    orgs: [Organization] = []
    for org in organizations:
        res = get_organization(org)
        if res is not None:
            orgs.append(res)
    return orgs


def get_user_organizations(user: AuthenticatedUser) -> ...:
    return user.get_orgs()


def get_pull_requests(organization: str, author: str, state: str) -> ...:
    query = 'org:{}'.format(organization)
    return list(api.search_issues(query, state=state, author=author, type='pr'))
