from soldier import Soldier
from unit import Unit


class Vehicle(Unit):
    def __init__(self, random=None):
        self.random = random
        self.__health = 100
        self.operators = []
        self.create_operators()

    def create_operators(self):
        for i in range(self.random.randint(1, 3)):
            self.operators.append(Soldier(self.random))

    @property
    def attack_success_probability(self):
        return 0.5 * (1 + self.health / 100) * sum(
            operator.attack_success_probability for operator in
            self.operators) / len(self.operators)

    @property
    def health(self):
        return sum(operator.health for operator in self.operators) / len(
            self.operators) + self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def damage(self):
        return 0.1 + sum(
            operator.experience for operator in self.operators) / 100

    def get_damage(self, damage):
        vehicle_damage = damage * 0.6
        operator_damage = damage * 0.1
        self.health -= vehicle_damage
        for operator in self.operators:
            operator.get_damage(operator_damage)

    def get_exp(self):
        for operator in self.operators:
            operator.get_exp()
