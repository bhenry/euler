from help import is_prime

m, A, B = 0, 0, 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while is_prime(n**2 + a*n + b):
            n += 1
        if n > m:
            m = n
            A = a
            B = b
print(A*B)
