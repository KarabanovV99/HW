y = input("Введите список: ")
lst = [x.strip() for x in y.split(",")]

def f(lst):
    d = {}

    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print("Элемент | Частота")
    for e, c in sorted_d:
        print(f"{str(e).ljust(7)} | {c:4}")

print(f(lst))