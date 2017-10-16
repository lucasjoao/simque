from numpy import random
from distribution import distribution


class normal(distribution):

    def __init__(self, average, dp):
        self.average = average
        self.dp = dp

    def generate(self):
        return random.normal(self.average, self.dp)
