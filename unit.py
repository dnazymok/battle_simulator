"""Unit module"""

from abc import ABC, abstractmethod


class Unit(ABC):
    """Abstract Unit class"""
    @property
    @abstractmethod
    def health(self):
        """Unit health

        Returns:
            health: int
        """

    @abstractmethod
    def get_damage(self, damage):
        """Get damage from enemy

        Args:
            damage:
        """
