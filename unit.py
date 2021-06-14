from abc import ABC, abstractmethod


class Unit(ABC):
    @property
    @abstractmethod
    def health(self):
        pass

    @property
    @abstractmethod
    def recharge(self):
        pass

