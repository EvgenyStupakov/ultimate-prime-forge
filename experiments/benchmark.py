import time

from generators.chaotic import ChaoticGenerator
from generators.wave import WaveGenerator
from generators.multi_wave import MultiWaveGenerator

from core.tests import miller_rabin


def benchmark(generator, name, attempts=100000):

    start = time.time()

    found = 0

    for _ in range(attempts):

        n = generator.next()

        if miller_rabin(n):

            found += 1

    elapsed = time.time() - start

    print(name)
    print("primes:", found)
    print("time:", elapsed)
    print("rate:", found/elapsed)
    print()


benchmark(ChaoticGenerator(), "Chaotic")
benchmark(WaveGenerator(), "Wave")
benchmark(MultiWaveGenerator(), "MultiWave")
