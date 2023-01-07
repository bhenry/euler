# Find the sum of all the primes below two million.
from help import is_prime


s = 0
for i in range(2, 2000000):
    if is_prime(i):
        s += i
print(s)
