l = 0
i = 0
s = '0.'
while l < 1000000:
    i += 1
    s += str(i)
    l += len(str(i))

print(int(s[2]) * int(s[11]) * int(s[101]) * int(s[1001]) * int(s[10001]) * int(s[100001]) * int(s[1000001]))
