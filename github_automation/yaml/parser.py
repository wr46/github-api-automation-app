from __future__ import annotations

import yaml
from typing import List

from github_automation.configuration.logger import instance
from github_automation.yaml.nodes import Node

logger = instance.get_logger()


class YamlData:
    def __init__(self):
        self.data = {}

    def add_nodes(self, nodes: List[Node]):
        for cls in Node.__subclasses__():
            tag = cls().yaml_tag()
            self.data[tag] = self.data.get(tag, []) + _get_node_by_type(nodes, cls)


def parse_yaml_document(yaml_path) -> YamlData:
    yaml_data = YamlData()
    for sub in Node.__subclasses__():
        node: Node = sub()
        data = _get_parsable_data(yaml_path, node)
        logger.debug(f'Node {data} from {yaml_path}')
        yaml_data.add_nodes(node.get_nodes(data))
    return yaml_data


def _get_node_by_type(nodes: List[Node], node_type: ...) -> List[Node]:
    return [node for node in nodes if isinstance(node, node_type)]


def _get_parsable_data(yaml_path: str, parsable: Node) -> ...:
    with open(yaml_path, 'r') as stream:
        data = yaml.safe_load(stream)
        return data.get(parsable.yaml_tag()) if isinstance(data, dict) else None
