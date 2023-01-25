i = 1
c = {}
while True:
    n = i**3
    s = ''.join(sorted(str(n)))
    if s in c:
        c[s].append(n)
    else:
        c[s] = [n]
    if len(c[s]) == 5:
        print(min(c[s]))
        break
    i += 1
