"""Soldier module"""
from unit import Unit


class Soldier(Unit):
    """Soldier class

    Attributes:
        random: Random instance for repeatability
        health: Value of Soldier health
        experience: Value of Soldier experience
        damage: Value of Soldier damage
        attack_success_probability: Chance to attack enemy

    """
    def __init__(self, random=None):
        self.random = random
        self._health = 100
        self._experience = 0

    @property
    def health(self):
        """Soldier health

        Returns:
            health: int
        """
        return self._health

    @health.setter
    def health(self, value):
        """Set Soldier health

        Returns:
            None
        """
        self._health = value

    @property
    def experience(self):
        """Unit experience

         Experience affects soldier damage

        Returns:
            experience: int
        """
        return self._experience

    @experience.setter
    def experience(self, value):
        """Set Soldier experience

        Args:
            value: Number of increasing

        Returns:
            None
        """
        if self.experience < 50:
            self._experience = value

    @property
    def damage(self):
        """Soldier damage

        Returns:
            int
        """
        return 0.05 + self.experience / 100

    @property
    def attack_success_probability(self):
        """Chance to attack enemy

        Returns:
            int
        """
        return 0.5 * (1 + self.health / 100) * self.random.randint(
            50 + self.experience,
            100) / 100

    def get_exp(self):
        """Increases the experience of units

        Returns:
            None
        """
        self.experience += 1

    def get_damage(self, damage):
        """Get damage from enemy

            Args:
                damage: int

            Returns:
                None
        """
        if self.health > 0:
            self.health -= damage
