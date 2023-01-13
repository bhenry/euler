s = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20 + 21 + 22 + 23

cache = {}

def is_abundant(n):
    if n in cache:
        return cache[n]
    divisors = [a for a in range(1, n) if n % a == 0]
    ret = sum(divisors) > n
    cache[n] = ret
    return ret

for i in range(24, 28124):
    two_abundant = False
    for j in range(1, i):
        if is_abundant(j) and is_abundant(i-j):
            two_abundant = True
            break
    if not two_abundant:
        s += i

print(s)
