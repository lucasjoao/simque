

class event(object):

    def __init__(self, entity, typ, time):
        self.entity = entity
        self.typ = typ  # 0 chegada, 1 saída
        self.time = time

    def __lt__(self, other):
        return self.time < other.time

    def execute(self):
        pass
