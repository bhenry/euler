# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
from decimal import *
# The period of 1/k for integer k is always ≤ k − 1.
getcontext().prec = 2000

fracts = []
for i in range(2, 1000):
    fract = str(Decimal(1)/Decimal(i))
    fracts.append(fract[fract.find('.')+1:])

# find longest repeating fraction chunk
m = 0
F = 0
for f in fracts:
    # start at 6 so i don't short circuit on 0.00...
    for i in range(6, len(f)//2):
        if f[:i] == f[i:i+i]:
            if i > m:
                m = i
                F = round(1/(Decimal(f".{f}")))
            break
print(F)
