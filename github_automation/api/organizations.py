from typing import List

from github import Organization, AuthenticatedUser

from github_automation.api.auth import api


def get_organization(organization: str) -> Organization:
    return api.get_organization(organization)


def get_organizations(organizations: List[str]) -> [Organization]:
    orgs: [Organization] = []
    for org in organizations:
        orgs.append(get_organization(org))
    return orgs


def get_user_organizations(user: AuthenticatedUser) -> ...:
    return user.get_orgs()
