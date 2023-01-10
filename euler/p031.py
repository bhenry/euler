# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# How many different ways can £2 be made using any number of coins?

# find all ways to make 200p with any number of 1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p

coins = [1, 2, 5, 10, 20, 50, 100, 200]
g = 200
# find all possible combinations of coins that add up to 200
combos = set()
combos.add((0,0,0,0,0,0,0,1))
for i in range(201):
    for j in range(101):
        if i + j*2 > g:
            break
        for k in range(41):
            if i + j*2 + k*5 > g:
                break
            for l in range(21):
                if i + j*2 + k*5 + l*10 > g:
                    break
                for m in range(11):
                    if i + j*2 + k*5 + l*10 + m*20 > g:
                        break
                    for n in range(5):
                        if i + j*2 + k*5 + l*10 + m*20 + n*50 > g:
                            break
                        for o in range(3):
                            if i + j*2 + k*5 + l*10 + m*20 + n*50 + o*100 == g:
                                combos.add((i, j, k, l, m, n, o, 0))
print(len(combos))
