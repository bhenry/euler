# Find the sum of the digits in the number 100!
from help import factorial
s = str(factorial(100))
print(sum(int(i) for i in s))
