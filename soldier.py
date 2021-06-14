from unit import Unit
from random import randint


class Soldier(Unit):
    def __init__(self):
        self.__health = 100
        self.__recharge = 100
        self.__experience = 0

    @property
    def health(self):
        return self.__health

    @property
    def recharge(self):
        return self.__recharge

    @property
    def experience(self):
        return self.__experience

    @property
    def attack_success_probability(self):
        return 0.5 * (1 + self.health / 100) * randint(50 + self.experience,
                                                       100) / 100

    @property
    def damage(self):
        return 0.05 + self.experience / 100
