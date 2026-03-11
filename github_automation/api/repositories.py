from typing import List, Optional

from github.Repository import Repository
from github.PullRequest import PullRequest
from github.AuthenticatedUser import AuthenticatedUser
from github.Organization import Organization
from github.ContentFile import ContentFile

from github_automation.configuration.logger import instance

logger = instance.get_logger()


class BranchData:
    def __init__(self, repository: Repository, name: str, src_branch_name: str):
        self.repository = repository
        self.name = name
        self.src_branch_name = src_branch_name


class CommitData:
    def __init__(self, message: str, file_path: str, content: bytes, sha: str):
        self.message = message
        self.file_path = file_path
        self.content = content
        self.sha = sha


class PullRequestData:
    def __init__(self, title: str, body: str, head_branch: str):
        self.title = title
        self.body = body
        self.head_branch = head_branch
        self.base_branch = None

    def set_base_branch(self, base_branch: str):
        self.base_branch = base_branch


def create_branch(branch: BranchData):
    repo = branch.repository
    branch_exists: bool
    try:
        source_branch = repo.get_branch(branch.src_branch_name)
        repo.create_git_ref(ref='refs/heads/' + branch.name, sha=source_branch.commit.sha)
    except:
        logger.error(f'Failed to create branch {branch.name}')


def create_commit(branch: BranchData, commit: CommitData):
    branch.repository.update_file(commit.file_path, commit.message, commit.content, commit.sha, branch.name)


def create_pull_request(pr: PullRequestData, repository: Repository) -> PullRequest:
    try:
        return repository.create_pull(title=pr.title, body=pr.body, head=pr.head_branch, base=pr.base_branch)
    except Exception as e:
        logger.warning(f'Failed to create PR in {repository.name} message: {e}')


def get_repository(repository: str, organization: Organization = None, user: AuthenticatedUser = None) -> Repository:
    assert organization is not None and user is not None, "Organization or AuthenticatedUser required!"
    return user.get_repo(repository) if organization is None else organization.get_repo(repository)


def get_org_repository_by_name(organization: Organization, name: str) -> Optional[Repository]:
    try:
        return organization.get_repo(name)
    except Exception as e:
        logger.error(f'Repository "{name}" not found in organization "{organization.login}": {e}')
        return None


def get_user_repositories(user: AuthenticatedUser) -> List[Repository]:
    return list(user.get_repos())


def get_user_repositories_by_name(user: AuthenticatedUser, names: List[str]) -> List[Repository]:
    return [user.get_repo(name) for name in names]


def get_repositories(
    organizations: Optional[List[Organization]] = None,
    user: Optional[AuthenticatedUser] = None
) -> List[Repository]:
    if organizations:
        repos = []
        for org in organizations:
            repos.extend(org.get_repos(type='all'))
        return repos
    elif user:
        return list(user.get_repos())
    else:
        raise ValueError("You must provide either a list of organizations or an authenticated user.")


def get_file_content(repository: Repository, branch: str, path: str) -> ContentFile:
    try:
        return repository.get_contents(path, ref=branch)
    except Exception as e:
        logger.error(f'Branch name="{branch}" or path="{path}" not found in repo="{repository.name}": {e}')


def update_file_content(repository: Repository, branch: str, path: str, message: str, sha: str, content: bytes):
    repository.update_file(path, message, content, sha, branch=branch)
