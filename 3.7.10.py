from collections import Counter

def long(t):

    longest = max(t, key=len)
    
    return longest

def coun(t):

    count = Counter(t)
    return count.most_common(1)[0][0]  # выводит вложенный картеж

lst = input("Введите список: ").split()

print("Самое длинное слово:", long(lst))
print("Наиболее часто встречаемое слово:", coun(lst))
