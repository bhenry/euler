from help import is_prime


def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
        if not is_prime(int(str(n)[:-i])):
            return False
    return True

s = 0
c = 0
i = 11
while c < 11:
    si = str(i)
    if si[0] in '2357' and not (set(si[1:]) - set('1379')):
        if is_truncatable_prime(i):
            s += i
            c += 1
    i += 2
print(s)
