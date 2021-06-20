""" Strategies module"""
from random import Random
from abc import ABC, abstractmethod

import settings


class BaseStrategy(ABC):
    """Abstract Strategy class"""
    @staticmethod
    @abstractmethod
    def select_enemy(enemies):
        """Selects an enemy based on a specific strategy

        Args:
            enemies: List of enemies, with attribute `health`

        Returns:
            enemy: Object from enemies list
        """


class StrategySelectStrongest(BaseStrategy):
    """Strategy that selects the strongest enemy"""
    @staticmethod
    def select_enemy(enemies):
        return sorted(enemies, key=lambda enemy: enemy.health, reverse=True)[0]


class StrategySelectWeakest(BaseStrategy):
    """Strategy that selects the weakest enemy"""
    @staticmethod
    def select_enemy(enemies):
        return sorted(enemies, key=lambda enemy: enemy.health)[0]


class StrategySelectRandom(BaseStrategy):
    """Strategy that selects the random enemy"""
    @staticmethod
    def select_enemy(enemies):
        return Random(settings.RANDOM_SEED).choice(enemies)
