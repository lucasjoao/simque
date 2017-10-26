

class event(object):

    def __init__(self, entity, typo, time, about_fail):
        self.entity = entity  # 1 ou 2
        self.typo = typo  # 0 chegada, 1 saída
        self.time = time
        self.about_fail = about_fail
        self.exec_time = 0

    def __lt__(self, other):
        return self.time < other.time
