from typing import Any

from github import Github


def get_user_repositories(api: Github) -> Any:
    return api.get_user().get_repos()
