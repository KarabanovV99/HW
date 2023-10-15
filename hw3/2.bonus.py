from itertools import permutations


def sled(chislo):
    lst = []
    for i in permutations(chislo):
        num = int(''.join(i))
        if num != int(chislo):
            lst.append(num)
    if len(lst) == 0:
        return -1
    sorted_lst = sorted(lst)
    for n in sorted_lst:
        if n > int(chislo):
            return str(n)
    return -1


print(sled(input("Число: ")))
