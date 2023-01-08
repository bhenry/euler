# Evaluate the sum of all the amicable numbers under 10000
def is_amicable(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    s2 = 0
    for i in range(1, s):
        if s % i == 0:
            s2 += i
    return s2 == n and s != n

s = 0
for i in range(1, 10000):
    if is_amicable(i):
        s += i
print(s)
