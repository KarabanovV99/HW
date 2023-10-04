def f():
    lst = []
    while True:
        n = input("input: ")
        if not n:
            break
        lst.append(n)
    return lst
print(f())