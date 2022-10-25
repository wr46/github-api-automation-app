from typing import Any

from github import Repository, PullRequest

from github_automation.api.auth import api
from github_automation.configuration.config import GITHUB_ORGANIZATION
from github_automation.main import logger


class CommitData:
    message: str
    file_path: str
    content: bytes
    sha: str


class BranchData:
    repository: Repository
    name: str


class PullRequestData:
    title: str
    body: str
    head_branch: BranchData
    base_branch: BranchData


def get_user_repositories() -> Any:
    org = GITHUB_ORGANIZATION
    return api.get_user().get_repos() if org == '' else api.get_organization(org).get_repos()


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
        logger.error(f'Failed to create branch { branch.name }')


def create_commit(branch: BranchData, commit: CommitData):
    branch.repository.update_file(commit.file_path, commit.message, commit.content, commit.sha, branch.name)


def create_pull_request(pr: PullRequestData, repository: Repository) -> PullRequest.PullRequest:
    return repository.create_pull(title=pr.title,
                                  body=pr.body,
                                  head=pr.head_branch,
                                  base=pr.base_branch)
