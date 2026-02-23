from generators.chaotic import ChaoticGenerator
from generators.wave import WaveGenerator
from generators.multi_wave import MultiWaveGenerator
from generators.hybrid import HybridGenerator

from core.tests import miller_rabin
from core.metrics import prime_energy

import time

generators = {
    "Chaotic"   : ChaoticGenerator(),
    "Wave"      : WaveGenerator(),
    "MultiWave" : MultiWaveGenerator(waves=6),
    "Hybrid"    : HybridGenerator(waves=6)
}

found_per_gen = {name:0 for name in generators}
max_primes = 20
heatmap_width = 50

print("=== ULTIMATE PRIME FORGE LAB v1.1 ===\n")

for name, gen in generators.items():
    print(f"--- {name} Generator ---\n")
    start = time.time()

    heatline = ""
    while found_per_gen[name] < max_primes:

        candidate = gen.next()
        energy = prime_energy(candidate, samples=12)

        if miller_rabin(candidate):
            found_per_gen[name] += 1

            num_hashes = int((0.1 - energy) * heatmap_width)
            num_hashes = max(1, num_hashes)
            heatline += "#" * num_hashes + " "

            print(f"{name} PRIME FOUND | {candidate} | energy: {energy:.4f} | {'#'*10}")
    
    elapsed = time.time() - start
    rate = found_per_gen[name] / elapsed

    print(f"\n{name} heatmap:\n{heatline}\n")
    print(f"{name} stats: primes={found_per_gen[name]} | time={elapsed:.2f}s | rate={rate:.2f} primes/sec\n")
