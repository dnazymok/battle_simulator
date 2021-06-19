import random
import strategies
import settings
from army import Army


class Game:
    strategies = [strategies.StrategySelectStrongest,
                  strategies.StrategySelectWeakest,
                  strategies.StrategySelectRandom]

    def __init__(self):
        self.armies = []
        self.create_armies()

    def create_armies(self):
        for i in range(settings.COUNT_OF_ARMIES):
            strategy = random.choice(Game.strategies)
            self.armies.append(Army(strategy))

    def filter_alive_armies(self):
        self.armies = [army for army in self.armies if army.squads]

    def run(self):
        while len(self.armies) > 1:
            for army in self.armies:
                if army.health <= 0:
                    break
                enemy_armies = [enemy_army for enemy_army in self.armies if
                                enemy_army is not army]
                enemy_army = army.strategy.select_enemy(enemy_armies)
                if army.attack_success_probability > enemy_army.attack_success_probability:
                    army.attack(enemy_army)
                    self.filter_alive_armies()
        print(self.armies)
