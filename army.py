import settings
from squad import Squad


class Army:
    def __init__(self):
        self.squads = []
        self.create_squads()

    def create_squads(self):
        for i in range(settings.COUNT_OF_SQUADS_PER_ARMY):
            self.squads.append(Squad())