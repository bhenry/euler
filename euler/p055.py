from help import is_palindrome

def is_lychrel(n):
    for i in range(50):
        n = n + int(str(n)[::-1])
        if is_palindrome(n):
            return False
    return True

s = 0
for i in range(1, 10000):
    if is_lychrel(i):
        s += 1
print(s)
