from generators.chaotic import ChaoticGenerator
from core.tests import miller_rabin
from core.metrics import prime_energy
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
gen = ChaoticGenerator()

found = 0

while found < 20:

    candidate = gen.next()

    energy = prime_energy(candidate)

    if energy < 0.1 and miller_rabin(candidate):

        print("PRIME FOUND")
        print("value :", candidate)
        print("energy:", energy)
        print()

        found += 1
