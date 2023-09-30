# from itertools import *

# x = [a for a in input().split()]
# print(max(list(permutations(x, r=len(x)))))

# x = [str(x) for x in input().split()]
# x = sorted(x, reverse=True)
lst = []
while True:
    n = input()
    if not n:
        break
    lst.append(n)

lst.sort(reverse=True)
print(''.join(lst))