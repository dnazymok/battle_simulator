import settings
from army import Army


class Game:
    def __init__(self):
        self.armies = []
        self.create_armies()

    def create_armies(self):
        for i in range(settings.COUNT_OF_ARMIES):
            self.armies.append(Army())


