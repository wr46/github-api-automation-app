from __future__ import annotations

import yaml
from typing import List
from abc import ABC, abstractmethod

from github_automation.configuration.logger import instance

logger = instance.get_logger()


class Node(ABC):
    @abstractmethod
    def get_yaml_tag(self) -> str:
        pass

    @abstractmethod
    def get_nodes(self, data: ...) -> List[Node]:
        pass


class Organization(Node):
    name: str

    def get_yaml_tag(self) -> str:
        return 'organizations'

    def get_nodes(self, data: ...) -> List[Node]:
        orgs = []
        for ele in data if data is not None else orgs:
            orgs.append(_build_parsable(self, {'name': ele}))
        return orgs


class Repository(Node):
    name: str
    branch: str

    def get_yaml_tag(self) -> str:
        return 'repositories'

    def get_nodes(self, data: ...) -> List[Node]:
        repos = []
        for repo in data if data is not None else repos:
            repos.append(_build_parsable(self, repo))
        return repos


class YamlData:
    def __init__(self):
        self.organizations: List[Node] = []
        self.repositories: List[Node] = []

    def add_nodes(self, nodes: List[Node]):
        self.organizations.extend(_get_node_by_type(nodes, Organization))
        self.repositories.extend(_get_node_by_type(nodes, Repository))


def parse_yaml_document(yaml_path) -> YamlData:
    yaml_data = YamlData()
    for node in _parse_nodes:
        data = _get_parsable_data(yaml_path, node)
        logger.debug(f'Node {data} from {yaml_path}')
        yaml_data.add_nodes(node.get_nodes(data))
    return yaml_data


def _get_node_by_type(nodes: List[Node], node_type: ...) -> List[Node]:
    return [node for node in nodes if isinstance(node, node_type)]


def _build_parsable(parsable: Node, pair: ...) -> Node:
    obj = object.__new__(parsable.__class__)
    for key, value in pair.items():
        setattr(obj, key, value)
    return obj


def _get_parsable_data(yaml_path: str, parsable: Node) -> ...:
    with open(yaml_path, 'r') as stream:
        data = yaml.safe_load(stream)
        return data[parsable.get_yaml_tag()]


_parse_nodes: List[Node] = [Organization(), Repository()]
