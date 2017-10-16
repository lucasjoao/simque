from distribution import distribution


class constant(distribution):

    def __init__(self, amount):
        self.amount = amount

    def generate(self):
        return self.amount
