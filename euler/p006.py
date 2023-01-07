# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum of the first one hundred natural numbers.

su, sq = 0, 0
for i in range(1, 101):
    su += i
    sq += i * i
print(su * su - sq)
