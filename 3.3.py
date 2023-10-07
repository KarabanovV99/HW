def f(n):    
    c1 = 1
    c2 = 1
    lst = []
    lst.append(c1)
    if n >= 2:
        lst.append(c2)
 
    for i in range(2, n):
        c1, c2 = c2, c1 + c2
        lst.append(c2)
    return lst

n = int(input("Сколько чисел вывести: "))

print(f(n))