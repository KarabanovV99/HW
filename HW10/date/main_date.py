from date import Date, ColorEnum, DateStamp


def main():
    voite = int(input(
        "{0}Введите 1, чтобы ввести дату вручную, или 2, чтобы ввести сегодняшнюю дату: {1}".format(ColorEnum.GREEN,
                                                                                                    ColorEnum.FINISH)))
    if voite == 1:
        d1 = Date()
        d1.input_date()
    elif voite == 2:
        d1 = DateStamp()
    else:
        print("{0}Incorrect choice. Try again{1}".format(ColorEnum.RED, ColorEnum.FINISH))
    print(ColorEnum.GREEN + "\n" + str(d1) + ColorEnum.FINISH)
    while True:
        print(ColorEnum.BLUE + "_" * 27 + ColorEnum.FINISH, '\n')
        print(ColorEnum.GREEN + "1. Отняти или добавить дни")
        print("2. Вычислить день недели")
        print("3. Сложить или вычесть даты")
        print("4. Exit" + ColorEnum.FINISH, "\n")

        choice = input("{0}Enter your choice: {1}".format(ColorEnum.YELLOW, ColorEnum.FINISH))
        print("")

        if choice == '1':
            num = int(input(
                "{0}Введите количество дней для корректировки: {1}".format(ColorEnum.YELLOW, ColorEnum.FINISH)))
            d1.adjust_days(num)
            print("\n", "{0}Новая дата после корректировки: {1}{2}".format(ColorEnum.GREEN, str(d1), ColorEnum.FINISH))

        elif choice == '2':
            print("{0}{1}{2}".format(ColorEnum.GREEN, d1.day_of_the_week(), ColorEnum.FINISH))

        elif choice == '3':
            choice_one = input("{0}Введите + для сложения и - для вычитания: {1}".format(ColorEnum.YELLOW, ColorEnum.FINISH))
            if choice_one == '+':
                d2 = Date()
                d2.input_date()
                print(d1 + d2)
            elif choice_one == '-':
                d2 = Date()
                d2.input_date()
                print(d1 - d2)
            else:
                print("{0}Incorrect choice{1}".format(ColorEnum.RED, ColorEnum.FINISH))

        elif choice == '4':
            break

        else:
            print("{0}Incorrect choice. Try again{1}".format(ColorEnum.RED, ColorEnum.FINISH))


if __name__ == "__main__":
    main()
