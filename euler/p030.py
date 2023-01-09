# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def can_it(n):
    return n == sum(int(d)**5 for d in str(n))

s = 0
for n in range(2, 1000000):
    if can_it(n):
        s += n
print(s)
