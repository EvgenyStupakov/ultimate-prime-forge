import math
import random

class HybridGenerator:

    def __init__(self, waves=4, seed=1):

        self.n = seed
        self.mod = 2**61 - 1

        # MultiWave parameters
        self.waves = []
        golden_ratio = (1 + 5**0.5) / 2

        for i in range(waves):
            omega = random.uniform(0.000001, 0.01) / (golden_ratio ** i)
            phi = random.uniform(0, 2*math.pi)
            amplitude = random.uniform(0.5, 1.5)
            self.waves.append((omega, phi, amplitude))

        # Chaotic component
        self.x = seed
        self.c = 17

        self.scale = 10**18

    def next(self):

        # Multi-wave sum
        wave_val = sum(amplitude * math.sin(omega * self.n + phi)
                       for omega, phi, amplitude in self.waves) / len(self.waves)

        # Chaotic addition
        self.x = (self.x*self.x + self.c) % self.mod
        chaotic_val = self.x / self.mod

        # Hybrid candidate
        value = abs(wave_val + chaotic_val)
        candidate = int(value * self.scale)

        self.n += 1
        candidate |= 1

        # eliminate trivial divisors
        if candidate % 3 == 0:
            candidate += 2
        if candidate % 5 == 0:
            candidate += 2

        return candidate % self.mod
