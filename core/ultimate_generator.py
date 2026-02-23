import time
from generators.chaotic import ChaoticGenerator
from generators.wave import WaveGenerator
from generators.multi_wave import MultiWaveGenerator
from generators.hybrid import HybridGenerator
from core.tests import miller_rabin

class UltimatePrimeGenerator:
    def __init__(self, waves=6):
        self.generators = {
            "Chaotic": ChaoticGenerator(),
            "Wave": WaveGenerator(),
            "MultiWave": MultiWaveGenerator(waves=waves),
            "Hybrid": HybridGenerator(waves=waves)
        }

    def generate(self, count=None, lower=None, upper=None, max_display=10, duration=None):
        found_per_gen = {name: 0 for name in self.generators}
        primes_list = {name: [] for name in self.generators}
        start_time = time.time()

        try:
            while True:
                elapsed = time.time() - start_time
                if duration and elapsed > duration:
                    break

                for name, gen in self.generators.items():
                    candidate = gen.next()

                    if lower is not None and candidate < lower:
                        continue
                    if upper is not None and candidate > upper:
                        continue

                    if miller_rabin(candidate):
                        found_per_gen[name] += 1
                        primes_list[name].append(candidate)

                        last_numbers = " ".join(str(p) for p in primes_list[name][-max_display:])
                        print(f"\r{name}: {last_numbers}", end=" " * 10, flush=True)

                        if count and found_per_gen[name] >= count:
                            continue

                if count and all(found_per_gen[name] >= count for name in self.generators):
                    break

        except KeyboardInterrupt:
            print("\nGeneration interrupted by user.")

        print("\n\n=== GENERATION ENDED ===\n")

        for name in self.generators:
            elapsed = time.time() - start_time
            rate = found_per_gen[name] / elapsed if elapsed > 0 else 0
            print(f"{name} stats: primes={found_per_gen[name]} | time={elapsed:.2f}s | rate={rate:.2f} primes/sec")
            print(f"Sample primes: {primes_list[name][:5]} ... {primes_list[name][-5:]}\n")

        return primes_list


def main():
    print("ULTIMATE PRIME GENERATOR CONSOLE \n")

    try:
        lower = int(input("Enter lower bound (e.g., 1e17): "))
        upper = int(input("Enter upper bound (e.g., 1e18): "))
        duration = int(input("Enter generation time in seconds (e.g., 30): "))
    except ValueError:
        print("Invalid input! Using defaults.")
        lower, upper, duration = 10**17, 10**18, 30

    print(f"\nGenerating primes in range [{lower}, {upper}] for {duration} seconds...\n")

    upg = UltimatePrimeGenerator(waves=6)
    primes = upg.generate(lower=lower, upper=upper, duration=duration, max_display=10)

    print("=== GENERATION COMPLETE ===\n")
    for gen_name, nums in primes.items():
        print(f"{gen_name} found {len(nums)} primes. Last 5 primes: {nums[-5:]}")
        print(f"Sample primes: {nums[:5]} ... {nums[-5:]}\n")

if __name__ == "__main__":
    main()
