from numpy import random
from impl.distribution import distribution


class exponential(distribution):

    def __init__(self, average):
        self.average = float(average)

    def generate(self):
        return int(random.exponential(self.average))
