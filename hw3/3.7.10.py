from collections import Counter


def long(t):
    return max(t, key=len)


def coun(t):
    count = Counter(t)
    return count.most_common(1)[0][0]  # [ ,[1]]


lst = input("Введите список: ").split()

print("Самое длинное слово:", long(lst))
print("Наиболее часто встречаемое слово:", coun(lst))
