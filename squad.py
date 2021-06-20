"""Squad module"""

import settings
from soldier import Soldier
from vehicle import Vehicle


class Squad:
    """Squad class

    Squad collects a group of units

    Attributes:
        random: Random instance for repeatability
        strategy: Instance of Strategy class
        units: List of units
        health: Sum health of self units
        damage: Sum damage of self units
        attack_success_probability: Average probability of self units

    """
    def __init__(self, strategy, random=None):
        self.random = random
        self.strategy = strategy
        self.units = []
        self.create_units()

    @property
    def health(self):
        """Squad health

            Returns:
                Sum of health of units in army
        """
        return sum(unit.health for unit in self.units)

    @property
    def damage(self):
        """Squad damage

            Returns:
                Sum of damage of units in army
        """
        return sum([unit.damage for unit in self.units])

    @property
    def attack_success_probability(self):
        """Squad probability to attack

        Returns:
            Average probability of squad units
        """
        return sum(
            [unit.attack_success_probability for unit in self.units]) / len(
            self.units)

    def create_units(self):
        """Fills units[] with Soldier or Vehicle instance

            Returns:
                 None
        """
        for _ in range(settings.COUNT_OF_UNITS_PER_SQUAD):
            self.units.append(self.random.choice(
                [Soldier(self.random), Vehicle(self.random)]))

    def get_damage(self, damage):
        """Get damage from another army

            Split up damage between units and checks if the amount of health
            has dropped < 0, in this case removes the unit from squad

            Args:
                damage: int

            Returns:
                None
        """
        for unit in self.units:
            unit.get_damage(damage)
            if unit.health < 0:
                self.units.remove(unit)

    def get_exp(self):
        """Increases the experience of units in the squad

        Returns:
            None
        """
        for unit in self.units:
            unit.get_exp()
