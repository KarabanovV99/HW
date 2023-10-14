def last_digit(a, b):
    if b == 0:             #любое число в 0 степени равно 1
        return 1

    last_digit_cycle = {   #заметим закономерность, последние цифра операции a ** b определяется последней цифрой a и имеет конечное число вариантов
        0: [0],  
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }

    last_digit_list = last_digit_cycle[a % 10] #находим последнюю цифру a
    last_digit_index = (b % len(last_digit_list)) - 1 #вычисляем какой именно вариант цифры нам нужен
    return last_digit_list[last_digit_index] #возвращаем последнюю цифру a ** b


print(last_digit(int(input("Число: ")), int(input("Степень: "))))
