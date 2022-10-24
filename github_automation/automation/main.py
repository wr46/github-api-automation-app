from typing import Callable, Any
from github import Github

from github_automation.api.auth import get_api
from github_automation.api.repositories import get_user_repositories


def execute(automation: Callable[[Any], None]):
    api = get_api()
    automation(api)


def list_repos(api: Github):
    for repo in get_user_repositories(api):
        print(repo.name)
