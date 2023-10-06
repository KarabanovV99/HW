def season(n):
    if 1 <= n <= 2 or n == 12:
        return "зима"
    elif 3 <= n <= 5:
        return "весна"
    elif 6 <= n <= 8:
        return "лето"
    else 9 <= n <= 11:
        return "осень"
print(season(int(input())))
