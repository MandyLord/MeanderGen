from abc import ABC, abstractmethod


class MotifBlueprint(ABC):

    @abstractmethod
    def build(self):
        pass