def long(t):

    slova = t.split()
    longest = ""

    for slovo in slova:
        if len(slovo) > len(longest):
            longest = slovo

    return longest


def cauntt(t):

    slova = t.split()
    slovoCountt = {}

    for slovo in slova:
        slovoCountt[slovo] = slovoCountt.get(slovo, 0) + 1

    return max(slovoCountt, key=slovoCountt.get)


t = input("Текст: ")

x = long(t)
y = cauntt(t)

print("Самое длинное слово:", x)
print("Наиболее часто встречаемое слово:", y)
