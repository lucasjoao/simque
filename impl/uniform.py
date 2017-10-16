from numpy import random
from distribution import distribution


class uniform(distribution):

    def __init__(self, mini, maxi):
        self.mini = mini
        self.maxi = maxi

    def generate(self):
        return random.uniform(self.mini, self.maxi)
