m = 0
for a in range(1,100):
    for b in range(1,100):
        s = sum(int(i) for i in str(a**b))
        if s > m:
            m = s
print(m)
