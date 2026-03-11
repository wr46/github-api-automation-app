from typing import List

from github import Repository, AuthenticatedUser

from github_automation.api import users, organizations, repositories
from github_automation.api.repositories import PullRequestData
from github_automation.automation.repositories.models import PullRequest
from github_automation.configuration.logger import instance
from github_automation.utils.content_handler.content_handler import ContentHandler

logger = instance.get_logger()


def list_repos(orgs: List[str], repos: List[str]):
    orgs: List[str] = organizations.get_organizations(orgs)
    for repo in repositories.get_repositories(orgs, users.get_user()):
        print(repo.name)


def list_user_open_prs(org: str, gh_username: str = None):
    user = users.get_user().login if gh_username is None else gh_username
    issues = organizations.get_pull_requests(org, user, 'open')
    for issue in issues:
        print(f'{issue.title};{issue.repository.name};{issue.html_url}')


def get_repos_default_branch(org: str, repos: List[str]) -> dict:
    gh_org = organizations.get_organization(org)
    gh_repos = repositories.get_repositories([gh_org], users.get_user())
    result: dict = {}
    for r in gh_repos:
        result[r.name] = r.default_branch

    return result


def create_prs(pull_requests: List[PullRequest]):
    for pr in pull_requests:
        pull_request = PullRequestData(pr.title, pr.body, pr.head_branch)
        if pr.organization is None:
            create_prs_by_user(pull_request, users.get_user(), [pr.repository])
        else:
            create_prs_by_organizations(pull_request, [pr.organization], [pr.repository])


def create_prs_by_organizations(pr: repositories.PullRequestData, orgs: List[str], repos: List[str]):
    repos_len: int = len(repos)
    for org_name in orgs:
        org = organizations.get_organization(org_name)
        for repo_name in repos:
            gh_repo = repositories.get_org_repository_by_name(org, repo_name)
            if pr.base_branch is None:
                pr.set_base_branch(gh_repo.default_branch)
            repositories.create_pull_request(pr, gh_repo)


def create_prs_by_user(pr: repositories.PullRequestData, user: AuthenticatedUser, repos_names: List[str]):
    repos: [Repository]
    if len(repos_names) == 0:
        repos = repositories.get_user_repositories(user)
    else:
        repos = repositories.get_user_repositories_by_name(user, repos_names)

    for repo in repos:
        repositories.create_pull_request(pr, repo)


def testing(repo: str):
    user = users.get_user()
    repos = repositories.get_user_repositories_by_name(user, [repo])

    for repo in repos:
        print(repo)
        look_for = "wdefwfw"
        content_handler = ContentHandler(repositories.get_file_content(repo, 'main', 'test.py'))
        content_handler.insert_line_by_str("awfaw", look_for)

        if content_handler.has_content_update is True:
            print(content_handler.content_decoded)
            #repositories.update_file_content(repo, 'main', content_handler.content_path, 'message', content_handler.content_sha, content_handler.content)
