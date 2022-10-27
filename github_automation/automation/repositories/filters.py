from typing import List


class RepositoriesFilter:
    def __init__(self, organizations: List[str] = None, repositories: List[str] = None):
        self.__organizations = organizations or []
        self.__repositories = repositories or []

    def get_organizations(self) -> List[str]:
        return self.__organizations

    def is_organizations_filtered(self, organizations: List[str]) -> bool:
        return _is_in_filter(organizations, self.__organizations)

    def get_repositories(self) -> List[str]:
        return self.__repositories

    def is_repository_filtered(self, repositories: List[str]) -> bool:
        return _is_in_filter(repositories, self.__repositories)


def _is_in_filter(to_find: List[str], to_filter: List[str]):
    if 0 == len(to_filter):
        return True

    if 0 == len(to_find):
        return False

    for elem in to_find:
        if elem not in to_filter:
            return False

    return True
