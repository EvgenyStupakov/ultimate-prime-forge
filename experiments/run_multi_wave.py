from generators.multi_wave import MultiWaveGenerator
from core.tests import miller_rabin
from core.metrics import prime_energy

gen = MultiWaveGenerator(waves=6)

found = 0

while found < 20:

    candidate = gen.next()

    energy = prime_energy(candidate)

    if energy < 0.1 and miller_rabin(candidate):

        print("MULTI-WAVE PRIME FOUND")
        print("value :", candidate)
        print("energy:", energy)
        print()

        found += 1
