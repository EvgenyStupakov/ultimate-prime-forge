import random

def prime_energy(n, samples=8):

    total = 0

    for _ in range(samples):

        a = random.randint(2, n - 2)

        value = pow(a, n-1, n)

        total += abs(value - 1)

    return total / samples
