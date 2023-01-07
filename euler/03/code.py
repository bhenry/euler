num = 600851475143
sqrt = int(num ** 0.5)
for i in range(sqrt, 1, -1):
    if num % i == 0 and all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
        print(i)
        break
