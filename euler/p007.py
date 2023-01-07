#What is the 10 001st prime number?

from help import is_prime

c = 0
lp = 2
n = 2
while c < 10001:
    if is_prime(n):
        c += 1
        lp = n
    n += 1
print(lp)
