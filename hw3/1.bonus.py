from functools import lru_cache


@lru_cache
def pascal(nomb_str, diog):

    lst = [[1] * (a + 1) for a in range(nomb_str)]

    for i in range(2, nomb_str):
        for j in range(1, i):
            lst[i][j] = lst[i-1][j-1] + lst[i - 1][j]

    sum = 0

    for u in lst:
        if diog < len(u):
            sum = sum + u[diog]

    return sum


nomb_str = int(input("Enter nomb_str: ")) + 1
diog = int(input("Enter diog: "))

print(pascal(nomb_str, diog))
