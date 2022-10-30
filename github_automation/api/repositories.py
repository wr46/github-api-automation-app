import sys
from typing import List

from github import Repository, PullRequest, AuthenticatedUser, Organization

from github_automation.configuration.logger import instance

logger = instance.get_logger()


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


def get_org_repositories(organization: Organization) -> ...:
    return organization.get_repos()


def get_org_repository_by_name(organization: Organization, name: str) -> Repository:
    return organization.get_repo(name)


def get_org_repositories_by_name(organization: Organization, names: List[str]) -> ...:
    repos: Repository = []
    for name in names:
        repos.append(get_org_repository_by_name(organization, name))

    return repos


def get_user_repositories(user: AuthenticatedUser) -> ...:
    return user.get_repos()


def get_user_repository_by_name(user: AuthenticatedUser, name: str) -> Repository:
    return user.get_repo(name)


def get_user_repositories_by_name(user: AuthenticatedUser, names: List[str]) -> [Repository]:
    repos: Repository = []
    for name in names:
        repos.append(get_user_repository_by_name(user, name))

    return repos


def get_repositories(repos: List[str], orgs: [Organization] = ..., user: AuthenticatedUser = ...) -> [Repository]:
    result: [Repository] = []
    if len(repos) > 0:
        if orgs is not None and len(orgs) > 0:
            for org in orgs:
                result.extend(get_org_repositories_by_name(org, repos))
        elif orgs is None and user is not None:
            result = get_user_repositories_by_name(user, repos)
        else:
            logger.warning(f'User and Organizations missing to fetch { repos } repositories')
    else:
        if orgs is None and user is not None:
            result = get_user_repositories(user)
        elif orgs is not None and len(orgs) > 0:
            for org in orgs:
                result.extend(get_org_repositories(org))
        else:
            logger.warning(f'User and Organizations missing to fetch all repositories')

    return result

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
        logger.log.error(f'Failed to create branch {branch.name}')


def create_commit(branch: BranchData, commit: CommitData):
    branch.repository.update_file(commit.file_path, commit.message, commit.content, commit.sha, branch.name)


def create_pull_request(pr: PullRequestData, repository: Repository) -> PullRequest.PullRequest:
    print(f'PR will be created for {repository.name}', file=sys.stderr)
    # return repository.create_pull(title=pr.title,
    #                             body=pr.body,
    #                              head=pr.head_branch,
    #                              base=pr.base_branch)
