from hesh import Hash


def main():
    h = Hash()

    while True:
        print("\033[31m" + "1. Добавить значение")
        print("2. Удалить значение")
        print("3. Получить значение")
        print("4. Коэффициент заполнения")
        print("5. Вывести таблицу")
        print("6. Выход" + "\033[0m")

        choice = input("\033[32m" + "Введите ваш выбор: " + "\033[0m")

        if choice == '1':
            key = input("\033[32m" + "Введите ключ: " + "\033[0m")
            value = input("\033[32m" + "Введите значение: " + "\033[0m")
            h.set_value(key, value)
        elif choice == '2':
            key = input("\033[32m" + "Введите ключ: " + "\033[0m")
            h.del_value(key)
        elif choice == '3':
            key = input("\033[32m" + "Введите ключ: " + "\033[0m")
            print(h.get_value(key))
        elif choice == '4':
            print(h.load())
        elif choice == '5':
            print(h.table)
        elif choice == '6':
            break
        else:
            print("\033[33m" + "Неверный выбор. Попробуйте еще раз." + "\033[0m")


if __name__ == "__main__":
    main()
