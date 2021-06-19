import settings
from soldier import Soldier


class Squad:
    def __init__(self, strategy):
        self.strategy = strategy
        self.units = []
        self.create_units()

    def create_units(self):
        for i in range(settings.COUNT_OF_UNITS_PER_SQUAD):
            self.units.append(Soldier())  # todo must be not soldier

    @property
    def attack_success_probability(self):
        return sum(
            [unit.attack_success_probability for unit in self.units]) / len(
            self.units)

    @property
    def damage(self):
        return sum([unit.damage for unit in self.units])
