from unit import Unit
from random import randint


class Soldier(Unit):
    def __init__(self):
        self.__health = 100
        self.__experience = 0

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        if self.experience < 50:
            self.__experience = value

    @property
    def attack_success_probability(self):
        return 0.5 * (1 + self.health / 100) * randint(50 + self.experience,
                                                       100) / 100

    @property
    def damage(self):
        return 5 + self.experience / 100

    def get_exp(self):
        self.experience += 1

    def get_damage(self, damage):
        if self.health > 0:
            self.health -= damage
