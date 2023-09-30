x = input()
if x.count('(') < x.count(')'):
    print("Не хватает '('")
elif x.count('(') > x.count(')'):
    print("Не хватает ')'")
else:
    print("Все скобки есть")