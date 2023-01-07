sum = 0
n = 1
n2 = 1
while n < 4000000:
    if n % 2 == 0:
        sum += n
    n, n2 = n2, n + n2
print(sum)
