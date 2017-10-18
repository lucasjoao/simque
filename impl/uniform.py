from numpy import random
from impl.distribution import distribution


class uniform(distribution):

    def __init__(self, mini, maxi):
        self.mini = float(mini)
        self.maxi = float(maxi)

    def generate(self):
        return int(random.uniform(self.mini, self.maxi))
