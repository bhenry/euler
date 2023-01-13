s = 0
for n in range(2, 1000000):
    if n == sum(int(d)**5 for d in str(n)):
        s += n
print(s)
