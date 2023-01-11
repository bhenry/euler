def possible_sides(perimeter):
    sides = []
    for a in range(1, perimeter):
        for b in range(a, perimeter):
            c = perimeter - a - b
            if c < b:
                break
            if a**2 + b**2 == c**2:
                sides.append((a, b, c))
    return sides

mx = 0
for i in range(1001):
    s = len(possible_sides(i))
    if s > mx:
        mx = s
        p = i
print(p)
