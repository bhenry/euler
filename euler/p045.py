from math import sqrt

def T(n):
    return n*(n+1)/2
def is_P(n):
    return (1 + sqrt(1 + 24*n)) % 6 == 0
def is_H(n):
    return (1 + sqrt(1 + 8*n)) % 4 == 0

i = 285
while True:
    i += 1
    t = T(i)
    if is_P(t) and is_H(t):
        print(int(t))
        break
