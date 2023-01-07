from math import sqrt


n = 1
t = 1
while True:
    n += 1
    t += n
    if len([i for i in range(1, int(sqrt(t))+1) if t % i == 0]) > 250:
        print(t)
        break
