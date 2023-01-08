from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))
