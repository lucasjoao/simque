from numpy import random
from impl.distribution import distribution


class triangular(distribution):

    def __init__(self, mini, mode, maxi):
        self.mini = float(mini)
        self.mode = float(mode)
        self.maxi = float(maxi)

    def generate(self):
        return int(random.triangular(self.mini, self.mode, self.maxi))
