def fib(n):
    f = [0, 1, 1]
    for _ in range(n - 2):
        f.append(f[-2] + f[-1])
    return f[:n]


print(fib(int(input())))
