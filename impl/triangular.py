from numpy import random
from distribution import distribution


class triangular(distribution):

    def __init__(self, mini, mode, maxi):
        self.mini = mini
        self.mode = mode
        self.maxi = maxi

    def generate(self):
        return random.triangular(self.mini, self.mode, self.maxi)
