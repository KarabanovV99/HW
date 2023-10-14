def season(n):
    if n in [1, 2, 12]:
        return "зима"
    if n in [3, 4, 5]:
        return "весна"
    if n in [6, 7, 8]:
        return "лето"
    if n in [9, 10, 11]:
        return "осень"
    return "ошибка"


print(season(int(input())))
