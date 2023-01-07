#What is the 10 001st prime number?

from math import sqrt


c = 0
lp = 2
def is_prime(n):
    for i in range(2, sqrt(n)):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            return True
    return False

while c < 10001:
    for i in range(2, sqrt(c)):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            c += 1
            if c == 10001:
                print(i)
