from itertools import permutations


def sled(chislo: str) -> str | int:
    lst = []
    for i in permutations(chislo):
        num = int(''.join(i))
        if num != int(chislo):
            lst.append(num)
    for n in sorted(lst):
        if n > int(chislo):
            return str(n)
    return -1


print(sled(input("Число: ")))
