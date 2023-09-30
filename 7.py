x = randint(0, 100)
y = int(input())
while y != x:
    if x < y:
        print("Число больше загадонного")
    else:
        print("число меньше загадонного")
    y = int(input())
print("угадал")
