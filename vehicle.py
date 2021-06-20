"""Vehicle module"""
from soldier import Soldier
from unit import Unit


class Vehicle(Unit):
    """Vehicle class

    Attributes:
        random: Random instance for repeatability
        health: Sum of operators health plus self health
        operators: List of Soldiers
        damage: Value of Vehicle damage
        attack_success_probability: Chance to attack enemy

    """
    def __init__(self, random=None):
        self.random = random
        self.__health = 100
        self.operators = []
        self.create_operators()

    @property
    def health(self):
        """Vehicle health

        Returns:
            health: int
        """
        return sum(operator.health for operator in self.operators) / len(
            self.operators) + self.__health

    @health.setter
    def health(self, value):
        """Set Vehicle health

        Returns:
            None
        """
        self.__health = value

    @property
    def damage(self):
        """Vehicle damage

        Returns:
            int
        """
        return 0.1 + sum(
            operator.experience for operator in self.operators) / 100

    @property
    def attack_success_probability(self):
        """Chance to attack enemy

        Returns:
            int
        """
        return 0.5 * (1 + self.health / 100) * sum(
            operator.attack_success_probability for operator in
            self.operators) / len(self.operators)

    def create_operators(self):
        """Fills operators[] with Soldier instance

            Returns:
                 None
        """
        for _ in range(self.random.randint(1, 3)):
            self.operators.append(Soldier(self.random))

    def get_damage(self, damage):
        """Get damage from enemy

            Args:
                damage: int

            Returns:
                None
        """
        vehicle_damage = damage * 0.6
        operator_damage = damage * 0.1
        self.health -= vehicle_damage
        for operator in self.operators:
            operator.get_damage(operator_damage)
            if operator.health < 0:
                self.operators.remove(operator)

    def get_exp(self):
        """Increases the experience of operators

        Returns:
            None
        """
        for operator in self.operators:
            operator.get_exp()
