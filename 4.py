x = input()
a = x.count('(')
b = x.count(')')
if a < b:
    print("Не хватает '('")
elif a > b:
    print("Не хватает ')'")
else:
    print("Все скобки есть")
