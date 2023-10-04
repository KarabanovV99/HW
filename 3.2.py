def f(n):
    if 1 <= n <= 2 or n == 12:
        return "зима"
    if 3 <= n <= 5:
        return "весна"
    if 6 <= n <= 8:
        return "лето"
    if 9 <= n <= 11:
        return "осень"
print(f(int(input())))