from numpy import random
from impl.distribution import distribution


class uniform(distribution):

    def __init__(self, min, max):
        self.min = min
        self.max = max

    def generate(self):
        return random.uniform(self.min, self.max)
