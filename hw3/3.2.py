def f(n):
    if n in [1, 2, 12]:
        return "зима"
    if n in [3, 4, 5]:
        return "весна"
    if n in [6, 7, 8]:
        return "лето"
    return "осень"

print(f(int(input())))