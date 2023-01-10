from math import sqrt


def binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

fibcache = {0: 0, 1: 1}
def fib(n):
    if n in fibcache:
        return fibcache[n]
    c = fib(n-1) + fib(n-2)
    fibcache[n] = c
    return c

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(abs(n)))+1):
        if n % i == 0:
            return False
    return True
