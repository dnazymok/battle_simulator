import random

from abc import ABC, abstractmethod


class BaseStrategy(ABC):
    @staticmethod
    @abstractmethod
    def select_enemy(enemies):
        pass


class StrategySelectStrongest(BaseStrategy):
    @staticmethod
    def select_enemy(enemies):
        return sorted(enemies, key=lambda enemy: enemy.health, reverse=True)[0]


class StrategySelectWeakest(BaseStrategy):
    @staticmethod
    def select_enemy(enemies):
        return sorted(enemies, key=lambda enemy: enemy.health)[0]


class StrategySelectRandom(BaseStrategy):
    @staticmethod
    def select_enemy(enemies):
        return random.choice(enemies)
