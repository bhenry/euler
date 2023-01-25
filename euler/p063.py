c = {}
e =
while True:
    for i in range(1, 10):
        if len(str(i ** e)) == e:
            c[e] = c.get(e, 0) + 1
    if len(str(9**e)) < e and len(str(10**e)) > e:
        break
    e += 1
print(sum(c.values()))
