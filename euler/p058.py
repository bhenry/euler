W = 1001
g = {}
l = (0,0)
facings = [(1,0), (0,-1), (-1,0), (0,1)]
f = -1
for i in range(W*W):
    if i == 0:
        g[(0,0)] = 1
        continue
    r = facings[(f + 1) % 4]
    n = (l[0] + r[0], l[1] + r[1])
    if n not in g:
        l = n
        g[l] = i + 1
        f = (f + 1) % 4
    else:
        l = (l[0] + facings[f][0], l[1] + facings[f][1])
        g[l] = i + 1

s = 0
for i in range(-(W//2),W//2+1):
    s += g[(i,i)]
    s += g[(i,-i)]
print(s - 1)
