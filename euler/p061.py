from math import sqrt

def is_triangle(n):
    return (sqrt(8*n+1)-1)/2 % 1 == 0
def is_square(n):
    return sqrt(n) % 1 == 0
def is_pentagonal(n):
    return (sqrt(24*n+1)+1)/6 % 1 == 0
def is_hexagonal(n):
    return (sqrt(8*n+1)+1)/4 % 1 == 0
def is_heptagonal(n):
    return (sqrt(40*n+9)+3)/10 % 1 == 0
def is_octagonal(n):
    return (sqrt(3*n+1)+1)/3 % 1 == 0

def follows(i):
    if i < 10:
        return []
    last2 = str(i)[2:4]
    if last2.startswith('0'):
        return []
    return range(int(last2 + '00'), int(str(int(last2) + 1) + '00'))

def all_repped(i, j, k, l, m, n):
    nums = {
        "tri": None,
        "squ": None,
        "pen": None,
        "hex": None,
        "hep": None,
        "oct": None,
    }
    for num in [i, j, k, l, m, n]:
        if is_triangle(num):
            nums["tri"] = num
        if is_square(num):
            nums["squ"] = num
        if is_pentagonal(num):
            nums["pen"] = num
        if is_hexagonal(num):
            nums["hex"] = num
        if is_heptagonal(num):
            nums["hep"] = num
        if is_octagonal(num):
            nums["oct"] = num
    if all(nums.values()) and len(set(nums.values())) == 6:
        print(nums)
        return True

for i in range (1000, 10000):
    if is_triangle(i) or is_square(i) or is_pentagonal(i) or is_hexagonal(i) or is_heptagonal(i) or is_octagonal(i):
        for j in follows(i):
            if is_triangle(j) or is_square(j) or is_pentagonal(j) or is_hexagonal(j) or is_heptagonal(j) or is_octagonal(j):
                for k in follows(j):
                    if is_triangle(k) or is_square(k) or is_pentagonal(k) or is_hexagonal(k) or is_heptagonal(k) or is_octagonal(k):
                        for l in follows(k):
                            if is_triangle(l) or is_square(l) or is_pentagonal(l) or is_hexagonal(l) or is_heptagonal(l) or is_octagonal(l):
                                for m in follows(l):
                                    if is_triangle(m) or is_square(m) or is_pentagonal(m) or is_hexagonal(m) or is_heptagonal(m) or is_octagonal(m):
                                        for n in follows(m):
                                            if not str(i).startswith(str(n)[2:4]):
                                                continue
                                            if is_triangle(n) or is_square(n) or is_pentagonal(n) or is_hexagonal(n) or is_heptagonal(n) or is_octagonal(n):
                                                if all_repped(i, j, k, l, m, n):
                                                    print(i + j + k + l + m + n)
                                                    exit()
