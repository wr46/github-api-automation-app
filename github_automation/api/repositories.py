import sys
from typing import List

from github import Repository, PullRequest, AuthenticatedUser, Organization

from github_automation.configuration.logger import get_logger

logger = get_logger()


class CommitData:
    def __init__(self, message: str, file_path: str, content: bytes, sha: str):
        self.message = message
        self.file_path = file_path
        self.content = content
        self.sha = sha


class BranchData:
    def __init__(self, repository: Repository, name: str):
        self.repository = repository
        self.name = name


class PullRequestData:
    def __init__(self, title: str, body: str, head_branch: str, base_branch: str):
        self.title = title
        self.body = body
        self.head_branch = head_branch
        self.base_branch = base_branch


def get_user_repositories(user: AuthenticatedUser) -> ...:
    return user.get_repos()


def get_org_repositories(organization: Organization) -> ...:
    return organization.get_repos()


def get_user_repositories_by_name(user: AuthenticatedUser, names: List[str]):
    repos: Repository = []
    for name in names:
        print(name)
        repos.append(user.get_repo(name))

    return repos


def create_pull_request_with_changes(branch: BranchData, commit: CommitData, pr: PullRequestData) -> str:
    create_branch(branch)
    create_commit(branch, commit)
    result = create_pull_request(pr)
    return result.html_url


def create_branch(branch: BranchData):
    repo = branch.repository
    branch_exists: bool
    try:
        source_branch = repo.get_branch('master')
        repo.create_git_ref(ref='refs/heads/' + branch.name, sha=source_branch.commit.sha)
    except:
        logger.error(f'Failed to create branch {branch.name}')


def create_commit(branch: BranchData, commit: CommitData):
    branch.repository.update_file(commit.file_path, commit.message, commit.content, commit.sha, branch.name)


def create_pull_request(pr: PullRequestData, repository: Repository) -> PullRequest.PullRequest:
    print(f'PR will be created for { repository.name }', file=sys.stderr)
    #return repository.create_pull(title=pr.title,
    #                             body=pr.body,
    #                              head=pr.head_branch,
    #                              base=pr.base_branch)
