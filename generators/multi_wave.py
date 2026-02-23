import math
import random

class MultiWaveGenerator:

    def __init__(self, waves=4, seed=1):

        self.n = seed
        self.mod = 2**61 - 1

        self.waves = []

        golden_ratio = (1 + 5**0.5) / 2

        for i in range(waves):

            omega = random.uniform(0.000001, 0.01) / (golden_ratio ** i)
            phi = random.uniform(0, 2*math.pi)
            amplitude = random.uniform(0.5, 1.5)

            self.waves.append((omega, phi, amplitude))

        self.scale = 10**18

    def next(self):

        value = 0.0

        for omega, phi, amplitude in self.waves:

            value += amplitude * math.sin(omega * self.n + phi)

        value /= len(self.waves)

        candidate = int(abs(value) * self.scale)

        self.n += 1

        candidate |= 1

        if candidate % 3 == 0:
            candidate += 2

        if candidate % 5 == 0:
            candidate += 2

        return candidate % self.mod
