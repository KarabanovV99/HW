def f():
    lst = []
    while True:
        n = input("input: ")
        if not n:
            break
        lst.append(n)
    return lst


def max_number(a):
    max_len = max(len(x) for x in a)
    a.sort(key=lambda x: x * max_len, reverse=True)
    return int(''.join(a))



print(max_number(f()))