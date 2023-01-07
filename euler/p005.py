import math


lcd = 1
for i in range(1, 21):
    lcd *= i // math.gcd(lcd, i)
print(lcd)

# 232792560
