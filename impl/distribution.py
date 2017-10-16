from abc import ABC, abstractmethod


class distribution(ABC):


    @abstractmethod
    def generate(self):
        pass
