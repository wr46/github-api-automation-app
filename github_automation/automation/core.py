from abc import abstractmethod, ABC
from typing import Optional, List

from github_automation.yaml.parser import parse_yaml_document, YamlData


class Context:
    base_path: str = './github_automation/configuration/context_files/'

    def __init__(self, yaml_file: str):
        yaml_data: YamlData = parse_yaml_document(self.base_path + yaml_file)
        self._map_to_context(yaml_data)

    def _map_to_context(self, yaml_data: YamlData):
        self.organizations: List[str] = [data.name for data in yaml_data.data['organizations']]
        self.repositories: List[str] = [data.name for data in yaml_data.data['repositories']]
        self.branches: List[str] = [data.name for data in yaml_data.data['branches']]
        self.commits: List[str] = [data.name for data in yaml_data.data['commits']]
        self.pull_requests: List[str] = [data.title for data in yaml_data.data['pullRequests']]


class Runnable(ABC):
    def __init__(self, yaml_path: str):
        self._context = Context(yaml_path)

    @abstractmethod
    def execute(self):
        pass

    def context(self) -> Optional[Context]:
        return self._context


def execute(runner: Runnable):
    runner.execute()
