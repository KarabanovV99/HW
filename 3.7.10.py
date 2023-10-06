from collections import Counter

def long(t):

    longest = max(t, key=len)
    
    return longest

def coun(t):

    count = Counter(t)
    
    return count.most_common(1)[0][0]

lst = input("Введите список: ").split()

print(long(lst), coun(lst))
