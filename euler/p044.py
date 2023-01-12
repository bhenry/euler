from math import sqrt

def pentagonal(n):
    return n*(3*n-1)/2

def is_pentagonal(n):
    return (1 + sqrt(1 + 24*n)) % 6 == 0

i = 0
diff = 5482660
while True:
    i += 1
    p = pentagonal(i)
    for j in range(i-1, 0, -1):
        q = pentagonal(j)
        if abs(p - q) > diff:
            break
        if is_pentagonal(p + q) and is_pentagonal(p - q):
            diff = abs(p - q)
    if i > 1000000:
        break

print(diff)
