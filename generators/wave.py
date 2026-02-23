import math
import random

class WaveGenerator:

    def __init__(self, seed=1):

        self.n = seed
        self.mod = 2**61 - 1

        # random wave parameters
        self.omega = random.uniform(0.000001, 0.01)
        self.phi = random.uniform(0, 2*math.pi)
        self.scale = 10**18

    def next(self):

        # wave evolution
        value = math.sin(self.omega * self.n + self.phi)

        # scale to large integer domain
        candidate = int(abs(value) * self.scale)

        self.n += 1

        # make odd
        candidate |= 1

        # eliminate trivial small divisors
        if candidate % 3 == 0:
            candidate += 2
        if candidate % 5 == 0:
            candidate += 2

        return candidate % self.mod
