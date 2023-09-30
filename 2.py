from itertools import *

x = [a for a in input().split()]
print(max(list(permutations(x, r=len(x)))))