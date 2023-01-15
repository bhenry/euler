c = 0

for i in range(1001):
    a = 1
    b = 2
    for j in range(i):
        a, b = b, 2 * b + a
    if len(str(a + b)) > len(str(b)):
        c += 1

print(c)
