from math import factorial


facts = {i: factorial(i) for i in range(10)}

def is_curious(n):
    return n == sum(facts[int(i)] for i in str(n))

s = 0
for i in range(10, 50000):
    if is_curious(i):
        print(i)
        s += i
print(s)
