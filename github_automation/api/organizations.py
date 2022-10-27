from github import Organization, AuthenticatedUser

from github_automation.api.auth import api


def get_organization(organization: str) -> Organization:
    return api.get_organization(organization)


def get_organizations(user: AuthenticatedUser) -> ...:
    return user.get_orgs()
