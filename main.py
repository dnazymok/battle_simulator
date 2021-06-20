from game import Game
import settings

random_seed = settings.RANDOM_SEED

if __name__ == "__main__":
    game = Game(random_seed)
    game.run()
