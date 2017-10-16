from numpy import random
from impl.distribution import distribution


class exponential(distribution):

    def __init__(self, average):
        self.average = average

    def generate(self):
        return random.exponential(self.average)
