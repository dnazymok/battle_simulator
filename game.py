"""Game module. Typical usage example:

    game = Game()
    game.run()

    Result of the game will be in the logs
"""
from random import Random

import strategies
import settings

from logger import TxtLogger
from army import Army


class Game:
    """Game class

    Needed to create armies and to fight them among themselves

    Attributes:
        random: Random instance for repeatability
        armies: List of armies
    """
    strategies = [strategies.StrategySelectStrongest,
                  strategies.StrategySelectWeakest,
                  strategies.StrategySelectRandom]

    def __init__(self, random_seed=None):
        self.random = Random(random_seed)
        self.armies = []
        self.create_armies()
        self.logger = TxtLogger()

    def create_armies(self):
        """Fills armies[] with Army instance

        Returns:
            None
        """
        for i in range(settings.COUNT_OF_ARMIES):
            strategy = self.random.choice(Game.strategies)
            self.armies.append(Army(f"Army {i + 1}", strategy, self.random))

    def filter_alive_armies(self):
        """Check army for the presence of squads in it

        If self.armies has no squads, it is removed from the self.armies

        Returns:
            None
        """
        self.armies = [army for army in self.armies if army.squads]

    def run(self):
        """Main loop

        Returns:
            None
        """
        while len(self.armies) > 1:
            for army in self.armies:
                if army.health <= 0:
                    break
                enemy_armies = [enemy_army for enemy_army in self.armies if enemy_army is not army]
                enemy_army = army.strategy.select_enemy(enemy_armies)
                if army.attack_success_probability > enemy_army.attack_success_probability:
                    self.logger.write(f"{army.name} attacks {enemy_army.name}")
                    army.attack(enemy_army)
                    self.filter_alive_armies()
                    for army in self.armies:
                        self.logger.write(f"{army.name} ---- {army.health} health")
        self.logger.close()
