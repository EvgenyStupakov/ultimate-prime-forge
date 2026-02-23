from generators.chaotic import ChaoticGenerator
from core.tests import fermat

gen = ChaoticGenerator()

found = 0

while found < 10:

    n = gen.next()

    if fermat(n, 12):

        print("prime:", n)
        found += 1
