from abc import abstractmethod, ABC
from typing import Optional, List

from github_automation.yaml.parser import parse_yaml_document, YamlData


class Context:
    def __init__(self, yaml_path: str):
        yaml_data: YamlData = parse_yaml_document(yaml_path)
        self._map_to_context(yaml_data)

    def _map_to_context(self, yaml_data: YamlData):
        self.organizations: List[str] = [org.name for org in yaml_data.organizations]
        self.repositories: List[str] = [repo.name for repo in yaml_data.repositories]


class Runnable(ABC):
    context: Context

    @abstractmethod
    def execute(self):
        pass

    def set_context(self, yaml_path: str):
        self.context = Context(yaml_path)

    def get_context(self) -> Optional[Context]:
        return self.context


def execute(runner: Runnable):
    runner.execute()
