from math import comb

c = 0
for i in range(1, 101):
    for j in range(1, i + 1):
        if comb(i, j) > 1000000:
            c += 1
print(c)
