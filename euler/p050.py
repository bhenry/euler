from help import is_prime

primes = [i for i in range(2, 1000000) if is_prime(i)]
max_len = 0
max_prime = 0
for i in range(len(primes)):
    for j in range(i + max_len, len(primes)):
        s = sum(primes[i:j])
        if s >= 1000000:
            break
        if is_prime(s):
            max_len = j - i
            max_prime = s
print(max_prime)
