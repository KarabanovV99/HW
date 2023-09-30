from random import randint

m = randint(0, 100)
n = int(input('input:'))
while m != n:
    if m > n:
        print('Загаданное число больше!')
    elif m < n:
        print('Загаданное число меньше!')
    else:
        print('Вы угадали число!')
        break
