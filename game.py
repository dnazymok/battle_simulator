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
