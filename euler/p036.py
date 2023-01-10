from help import is_palindrome

ps = []
for i in range(1000000):
    b = bin(i)[2:]
    if is_palindrome(i) and is_palindrome(b):
        ps.append(i)
print(sum(ps))
