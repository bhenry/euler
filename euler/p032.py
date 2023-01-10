def pandigital(a, b, c):
    s = str(a) + str(b) + str(c)
    return len(s) == 9 and set(s) == set('123456789')

products = set()
for a in range(1, 100):
    for b in range(100, 10000):
        c = a * b
        if pandigital(a, b, c):
            products.add(c)
print(sum(products))
