from help import is_prime

square = 1
d = 1
pds = 0
ds = 1
while True:
    a = d + 2 * square
    b = a + 2 * square
    c = b + 2 * square
    d = c + 2 * square
    square += 1
    ds += 4
    for n in (a,b,c,d):
        if is_prime(n):
            pds += 1
    if pds / ds < 0.1:
        break

print(2 * square - 1)
