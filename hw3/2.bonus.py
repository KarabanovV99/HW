# from itertools import permutations


# def sled(chislo):
#     lst = []
#     for i in permutations(chislo):
#         lst.append(i)
#     chislo = int(chislo)
#     sorted_lst = sorted(lst, key=lambda x: abs(x - chislo))
#     for n in sorted_lst:
#         if n > chislo:
#             return n
#     return None


# print(sled("21"))

# from itertools import permutations

# def sled(chislo):
#     lst = []
#     for i in permutations(chislo):
#         lst.append(int(''.join(i)))
#     chislo = int(chislo)
#     sorted_lst = sorted(lst)
#     for n in sorted_lst:
#         if n > chislo:
#             return str(n)
#     return None

# print(sled("123456"))


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
