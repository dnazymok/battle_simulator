"""Army module"""
import settings
from squad import Squad


class Army:
    """Army class

    Army collects a group of squads

    Attributes:
        random: Random instance for repeatability
        strategy: Instance of Strategy class
        squads: List of squads
        health: Sum health of self squads
        damage: Sum damage of self squads
        attack_success_probability: Average probability of self squads

    """
    def __init__(self, strategy, random=None):
        self.random = random
        self.strategy = strategy
        self.squads = []
        self.create_squads()

    @property
    def health(self):
        """Army health

        Returns:
            Sum of health of squads in army
        """
        return sum(squad.health for squad in self.squads)

    @property
    def damage(self):
        """Army damage

        Returns:
            Sum of damage of squads in army
        """
        return sum([squad.damage for squad in self.squads])

    @property
    def attack_success_probability(self):
        """Army probability to attack

        Returns:
            Average probability of army squads
        """
        return sum(
            [squad.attack_success_probability for squad in self.squads]) / len(
            self.squads)

    def create_squads(self):
        """Fills squads[] with Squad instance

        Returns:
             None
        """
        for _ in range(settings.COUNT_OF_SQUADS_PER_ARMY):
            self.squads.append(Squad(self.strategy, self.random))

    def attack(self, enemy_army):
        """Attack enemy

        Args:
            enemy_army: Army instance

        Returns:
            None
        """
        enemy_army.get_damage(self.damage)
        for squad in self.squads:
            squad.get_exp()

    def get_damage(self, damage):
        """Get damage from another army

        Args:
            damage: int

        Returns:
            None
        """
        for squad in self.squads:
            squad.get_damage(damage)
            if squad.health <= 0:
                self.squads.remove(squad)
