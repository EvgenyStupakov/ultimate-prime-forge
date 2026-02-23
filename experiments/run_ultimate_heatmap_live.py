import time
from generators.chaotic import ChaoticGenerator
from generators.wave import WaveGenerator
from generators.multi_wave import MultiWaveGenerator
from generators.hybrid import HybridGenerator
from core.tests import miller_rabin
from core.metrics import prime_energy

generators = {
    "Chaotic"   : ChaoticGenerator(),
    "Wave"      : WaveGenerator(),
    "MultiWave" : MultiWaveGenerator(waves=6),
    "Hybrid"    : HybridGenerator(waves=6)
}

heatmap_width = 50
found_per_gen = {name: 0 for name in generators}
heatlines = {name: "" for name in generators}
primes_list = {name: [] for name in generators}

duration = 30
start_time = time.time()

print("=== ULTIMATE PRIME FORGE LAB v1.3 (LIVE TIMER) ===\n")

while time.time() - start_time < duration:

    for name, gen in generators.items():
        candidate = gen.next()
        energy = prime_energy(candidate, samples=12)

        if miller_rabin(candidate):
            found_per_gen[name] += 1
            primes_list[name].append(candidate)

            num_hashes = int((0.1 - energy) * heatmap_width)
            num_hashes = max(1, num_hashes)
            heatlines[name] += "#" * num_hashes + " "

            last_numbers = " ".join(str(p) for p in primes_list[name][-5:])
            print(f"\r{name} heatmap: {heatlines[name]} | last: {last_numbers}", end="", flush=True)

    time.sleep(0.01)

print("\n\n=== TIMER ENDED ===\n")

for name in generators:
    elapsed = time.time() - start_time
    rate = found_per_gen[name] / elapsed
    print(f"{name} stats: primes={found_per_gen[name]} | time={elapsed:.2f}s | rate={rate:.2f} primes/sec")
    print(f"Sample primes: {primes_list[name][:5]} ... {primes_list[name][-5:]}\n")
