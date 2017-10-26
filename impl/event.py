

class event(object):

    def __init__(self, entity, typo, time, about_fail):
        self.entity = entity  # 1 or 2
        self.typo = typo  # 0 is entry, 1 is exit
        self.time = time
        self.about_fail = about_fail
        self.exec_time = 0
        self.init_time = 0

    def __lt__(self, other):
        return self.time < other.time

    def __repr__(self):
        return "Entity: {} Time: {}".format(self.entity, self.time)
