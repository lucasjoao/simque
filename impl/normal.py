from numpy import random
from impl.distribution import distribution


class normal(distribution):

    def __init__(self, average, dp):
        self.average = float(average)
        self.dp = float(dp)

    def generate(self):
        return int(random.normal(self.average, self.dp))
