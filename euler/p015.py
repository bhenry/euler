# find all routes through a 20×20 grid

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

print(binomial(40, 20))
