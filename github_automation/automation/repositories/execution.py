from github_automation.api.repositories import get_user_repositories


def list_repos():
    for repo in get_user_repositories():
        print(repo.name)
