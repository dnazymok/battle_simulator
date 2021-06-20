"""Main module"""

from game import Game
import settings

RANDOM_SEED = settings.RANDOM_SEED

if __name__ == "__main__":
    game = Game(RANDOM_SEED)
    game.run()
