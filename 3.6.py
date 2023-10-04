def f(n):
    lst = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            lst.append(i)
            lst.append(n // i)
    lst = set(lst)
    if len(lst) == 2:
        return True
    else:
        return False

x = int(input())

print(f(x))