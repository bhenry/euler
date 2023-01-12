from itertools import permutations
from help import is_prime, is_pandigital

digits = range(1,10)
candidates = []
for dig in digits[2:]:
    digs = digits[:dig]
    perms = permutations(digs)
    for p in perms:
        n = int("".join(map(str, p)))
        if is_prime(n):
            candidates.append(n)
print(max(candidates))
