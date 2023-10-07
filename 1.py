def f():
    lst = []

    while True:
        n = input("input: ")
        if not n:
            break
        lst.append(n)

    return lst

def s_list(lst, n):
    
    n %= len(lst)

    return lst[-n:] + lst[:-n]

print(s_list(f(), int(input("Введите число сдвига: "))))