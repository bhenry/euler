from help import fib


i = 1
while True:
    if len(str(fib(i))) > 999:
        print(i)
        break
    i += 1
