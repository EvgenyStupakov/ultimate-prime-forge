from generators.hybrid import HybridGenerator
from core.tests import miller_rabin
from core.metrics import prime_energy

gen = HybridGenerator(waves=6)

found = 0

while found < 20:

    candidate = gen.next()
    energy = prime_energy(candidate, samples=12)

    if energy < 0.1 and miller_rabin(candidate):

        # визуальный принт: чем меньше энергия → больше #
        bar = '#' * int((0.1 - energy) * 100)
        print(f"HYBRID PRIME FOUND | {candidate} | energy: {energy:.4f} | {bar}")

        found += 1
