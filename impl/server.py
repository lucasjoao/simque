

class server(object):

    def __init__(self, distribution, limited):
        self.distribution = distribution
        self.free = True
        self.with_error = False
        self.ef = 0
        self.limited = limited

    def work(self):
        return self.distribution.generate()
