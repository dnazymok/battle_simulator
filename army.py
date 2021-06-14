import settings
from squad import Squad


class Army:
    def __init__(self):
        self.squads = []

    def add_squad(self, squad):
        self.squads.append(squad)

    def fill_army_with_squads(self):
        for i in range(settings.COUNT_OF_SQUADS_PER_ARMY):
            squad = Squad()
            self.add_squad(squad)
