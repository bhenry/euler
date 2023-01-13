nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perms = []
for n in nums:
    for m in [a for a in nums if a != n]:
        for o in [a for a in nums if a != n and a != m]:
            for p in [a for a in nums if a != n and a != m and a != o]:
                for q in [a for a in nums if a != n and a != m and a != o and a != p]:
                    for r in [a for a in nums if a != n and a != m and a != o and a != p and a != q]:
                        for s in [a for a in nums if a != n and a != m and a != o and a != p and a != q and a != r]:
                            for t in [a for a in nums if a != n and a != m and a != o and a != p and a != q and a != r and a != s]:
                                for u in [a for a in nums if a != n and a != m and a != o and a != p and a != q and a != r and a != s and a != t]:
                                    for v in [a for a in nums if a != n and a != m and a != o and a != p and a != q and a != r and a != s and a != t and a != u]:
                                        perms.append(str(n) + str(m) + str(o) + str(p) + str(q) + str(r) + str(s) + str(t) + str(u) + str(v))

print(sorted(perms)[999999])
