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

prime_cache = {2: True}
def is_prime(n):
    if n in prime_cache:
        return prime_cache[n]
    if n < 2:
        return False
    for i in range(2, int(sqrt(abs(n)))+1):
        if n % i == 0:
            prime_cache[n] = False
            return False
    prime_cache[n] = True
    return True

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

def is_pandigital(s):
    if len(s) != 9:
        return False
    if set(s) != set('123456789'):
        return False
    return True
