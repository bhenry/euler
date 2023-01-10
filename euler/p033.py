from decimal import Decimal
egs = []
for a in range(10,99):
    for b in range(a,100):
        if a%10==0 and b%10==0:
            continue
        common = set(str(a)) & set(str(b))
        if len(common) == 0:
            continue
        common = common.pop()
        a1 = str(a).replace(common, '')
        b1 = str(b).replace(common, '')
        if not a1 or not b1:
            continue
        a1 = int(a1)
        b1 = int(b1)
        if a != b and a1 and b1 and a/b == a1/b1:
            egs.append((a,b))

p = 1
for pair in egs:
    p *= Decimal(pair[0])/Decimal(pair[1])
print(int(1/p))
