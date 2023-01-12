from help import is_prime
from itertools import count

def is_goldbach(n):
    for i in range(1, int(n**0.5)+1):
        if is_prime(n-2*i**2):
            return True
    return False

c = count(9, 2)
while True:
    n = next(c)
    if is_prime(n):
        continue
    if not is_goldbach(n):
        print(n)
        break
