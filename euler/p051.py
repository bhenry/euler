from help import is_prime

i = 1
while True:
    i += 2
    if not is_prime(i):
        continue
    s = str(i)
    for j in range(1, len(s)):
        b = int("1" * len(s), 2)
        for k in range(b):
            bs = bin(k)[2:]
            cs = set()
            for l in range(10):
                t = ""
                for x,y in zip(s, bs):
                    if y == '1':
                        t += str(l)
                    else:
                        t += x
                if t[0] == '0':
                    continue
                if is_prime(int(t)):
                    cs.add(int(t))
            if len(cs) == 8:
                print(min(cs))
                exit()
