from abc import ABC, abstractmethod


class Unit(ABC):
    @property
    @abstractmethod
    def health(self):
        pass

    @abstractmethod
    def get_damage(self, damage):
        pass
