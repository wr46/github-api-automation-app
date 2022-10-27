from github import AuthenticatedUser, PaginatedList, NamedUser

from github_automation.api.auth import api


def get_user() -> AuthenticatedUser:
    return api.get_user()


def get_users() -> ...:
    return api.get_users()
