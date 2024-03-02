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
        print(ColorEnum.RED + "Incorrect choice. Try again" + ColorEnum.FINISH)
    print(ColorEnum.GREEN + "\n" + str(d1) + ColorEnum.FINISH)
    while True:
        print(ColorEnum.BLUE + "_" * 27 + ColorEnum.FINISH, "\n")
        print(ColorEnum.GREEN + "1. Отняти или добавить дни")
        print("2. Вычислить день недели")
        print("3. Exit" + ColorEnum.FINISH, "\n")

        choice = input(ColorEnum.YELLOW + "Enter your choice: " + ColorEnum.FINISH)
        print("")

        if choice == '1':
            num = int(input(ColorEnum.YELLOW + "Введите количество дней для корректировки: " + ColorEnum.FINISH))
            d1.adjust_days(num)
            print("\n", ColorEnum.GREEN + "Новая дата после корректировки: " + str(d1) + ColorEnum.FINISH)

        elif choice == '2':
            print(ColorEnum.GREEN + d1.day_of_the_week() + ColorEnum.FINISH)

        elif choice == '3':
            break

        else:
            print(ColorEnum.RED + "Incorrect choice. Try again" + ColorEnum.FINISH)


if __name__ == "__main__":
    main()
