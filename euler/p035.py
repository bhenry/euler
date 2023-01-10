from help import is_prime

def is_circular_prime(n):
    n = str(n)
    for i in range(len(n)):
        if not is_prime(int(n)):
            return False
        n = n[1:] + n[0]
    return True

circular_primes = []
for i in range(2,1000000):
    if is_prime(i):
        if is_circular_prime(i):
            circular_primes.append(i)

print(len(circular_primes))
