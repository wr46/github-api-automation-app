from abc import abstractmethod, ABC


class Runnable(ABC):
    @abstractmethod
    def execute(self):
        pass


def execute(runner: Runnable):
    runner.execute()
