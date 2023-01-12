from help import is_pandigital

mx = 0
n = 1
lim = 987654321
while n < 10000:
    n += 1
    m = 2
    biggest = 0
    while biggest <= lim:
        t = ""
        for dig in range(1,m+1):
            t += str(n * dig)
        if is_pandigital(t):
            mx = max(mx, int(t))
        biggest = int(t)
        m += 1
print(mx)
