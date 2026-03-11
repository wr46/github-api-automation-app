from abc import ABC, abstractmethod
from typing import List


class Node(ABC):
    @abstractmethod
    def yaml_tag(self) -> str:
        pass

    def get_nodes(self, data: ...) -> List['Node']:
        nodes = []
        for node in data if data is not None else nodes:
            nodes.append(_build_parsable(self, node))
        return nodes


def _build_parsable(parsable: Node, pair: ...) -> Node:
    obj = object.__new__(parsable.__class__)
    for key, value in pair.items():
        setattr(obj, key, value)
    return obj


class Organization(Node):
    name: str

    def yaml_tag(self) -> str:
        return 'organizations'


class Repository(Node):
    name: str

    def yaml_tag(self) -> str:
        return 'repositories'


class Branch(Node):
    name: str

    def yaml_tag(self) -> str:
        return 'branches'


class Commit(Node):
    name: str
    message: str
    filePath: str

    def yaml_tag(self) -> str:
        return 'commits'


class PullRequest(Node):
    title: str
    body: str
    branch: str

    def yaml_tag(self) -> str:
        return 'pullRequests'
