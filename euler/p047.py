from help import is_prime

def get_prime_factors(n):
    factors = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if is_prime(n):
        factors.append(n)
    return factors

store = [
    set(),
    set(get_prime_factors(1)),
    set(get_prime_factors(2)),
    set(get_prime_factors(3)),
]
i = 4
while True:
    store = store[1:] + [set(get_prime_factors(i))]
    if len(store[0]) != 4 or len(store[1]) != 4 or len(store[2]) != 4 or len(store[3]) != 4:
        i += 1
        continue
    print(i - 3)
    break
