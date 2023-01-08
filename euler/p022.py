from inputs.p022_names import names

cscore = lambda name: sum(ord(c) - 64 for c in name)

s = 0
for i, n in enumerate(sorted(names)):
    s += cscore(n) * (i+1)
print(s)
