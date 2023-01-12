from itertools import permutations

ds = range(10)
ps = permutations(ds)
su = 0
for p in ps:
    s = "".join(str(d) for d in p)
    if p[0] == 0:
        continue
    if int(s[1:4]) % 2 != 0:
        continue
    if int(s[2:5]) % 3 != 0:
        continue
    if int(s[3:6]) % 5 != 0:
        continue
    if int(s[4:7]) % 7 != 0:
        continue
    if int(s[5:8]) % 11 != 0:
        continue
    if int(s[6:9])  % 13 != 0:
        continue
    if int(s[7:10]) % 17 != 0:
        continue
    su += int(''.join(str(d) for d in s))
print(su)
