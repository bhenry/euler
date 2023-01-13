from help import is_prime

primes = [i for i in range(1000, 10000) if is_prime(i)]
for i in range(len(primes)-2):
    for j in range(i+1, len(primes)-1):
        for k in range(j+1, len(primes)):
            if primes[i] + primes[k] == 2 * primes[j]:
                if set(str(primes[i])) == set(str(primes[j])) == set(str(primes[k])):
                    print(primes[i], primes[j], primes[k])
