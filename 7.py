from random import *

m = randint(0, 100)
while True:
    n = int(input('input'))
    if n < 1:
        print('число не подходит!')
        break
    if m > n:
        print('Загаданное число больше!')
    elif m < n:
        print('Загаданное число меньше!')
    else:
        print('Вы угадали число!')
        break
