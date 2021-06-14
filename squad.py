import settings
from soldier import Soldier


class Squad:
    def __init__(self):
        self.units = []

    def add_unit(self, unit):
        self.units.append(unit)

    def fill_squad_with_units(self):
        for i in range(settings.COUNT_OF_UNITS_PER_SQUAD):
            unit = Soldier()
            self.add_unit(unit)

    @property
    def attack_success_probability(self):
        return sum(
            [unit.attack_success_probability for unit in self.units]) / len(
            self.units)

    @property
    def damage(self):
        return sum([unit.damage for unit in self.units])
