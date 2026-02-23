class ChaoticGenerator:

    def __init__(self, seed=123456789):

        self.x = seed

        self.mod = 2**61 - 1
        self.c = 17

    def next(self):

        # chaotic evolution
        self.x = (self.x*self.x + self.c) % self.mod

        n = self.x | 1

        # eliminate trivial composites
        if n % 3 == 0:
            n += 2

        if n % 5 == 0:
            n += 2

        return n
