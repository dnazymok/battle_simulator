import settings
from squad import Squad


class Army:
    def __init__(self, strategy, random=None):
        self.random = random
        self.strategy = strategy
        self.squads = []
        self.create_squads()

    def create_squads(self):
        for i in range(settings.COUNT_OF_SQUADS_PER_ARMY):
            self.squads.append(Squad(self.strategy, self.random))

    def attack(self, enemy_army):
        enemy_army.get_damage(self.damage)
        for squad in self.squads:
            squad.get_exp()

    def get_damage(self, damage):
        for squad in self.squads:
            squad.get_damage(damage)
            if squad.health <= 0:
                self.squads.remove(squad)

    @property
    def health(self):
        return sum(squad.health for squad in self.squads)

    @property
    def damage(self):
        return sum([squad.damage for squad in self.squads])

    @property
    def attack_success_probability(self):
        return sum(
            [squad.attack_success_probability for squad in self.squads]) / len(
            self.squads)
