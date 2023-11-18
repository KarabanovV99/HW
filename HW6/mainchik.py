from heshhhhhhhh import *


def main():
    size: int = 10
    table = init_table(size)
    while True:
        print(COLORS["red"] + "1. Добавить значение")
        print("2. Удалить значение")
        print("3. Получить значение")
        print("4. Коэффициент заполнения")
        print("5. Вывести таблицу")
        print("6. Выход" + COLORS["finish"])

        choice = input(COLORS["green"] + "Введите ваш выбор: " + COLORS["finish"])

        if choice == '1':
            key = input(COLORS["green"] + "Введите ключ: " + COLORS["finish"])
            value = input(COLORS["green"] + "Введите значение: " + COLORS["finish"])
            size, table = set_value(key, value, table, size)

        elif choice == '2':
            key = input(COLORS["green"] + "Введите ключ: " + COLORS["finish"])
            table = del_value(key, table, size)

        elif choice == '3':
            key = input(COLORS["green"] + "Введите ключ: " + COLORS["finish"])
            print(get_value(key, table, size))

        elif choice == '4':
            print("Table size:", size)
            for i in range(size):
                if table[i]:
                    print("■", end="")
                else:
                    print("□", end="")
            print("\n", load(table))

        elif choice == '5':
            print(table)

        elif choice == '6':
            break

        else:
            print(COLORS["yellow"] + "Неверный выбор. Попробуйте еще раз." + COLORS["finish"])


if __name__ == "__main__":
    main()
