from random import randint

m = randint(0, 100)
while True:
    n = int(input('input:'))
    if m > n:
        print('Загаданное число больше!')
    elif m < n:
        print('Загаданное число меньше!')
    else:
        print('Вы угадали число!')
        break
