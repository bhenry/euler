i = 0
while True:
    i += 1
    if all(sorted(str(i)) == sorted(str(i * j)) for j in range(2, 7)):
        print(i)
        break
