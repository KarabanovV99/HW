from hash_table import HashTable, ColorEnum


def main():
    hash_table = HashTable()
    while True:
        print(ColorEnum.BLUE + "_" * 27 + ColorEnum.FINISH, "\n")
        print(ColorEnum.GREEN + "1. Add value")
        print("2. Delete value")
        print("3. Get value")
        print("4. Fill factor")
        print("5. Print dictionary")
        print("6. Exit" + ColorEnum.FINISH, "\n")

        choice = input(ColorEnum.YELLOW + "Enter your choice: " + ColorEnum.FINISH)
        print("")

        if choice == '1':
            key = input(ColorEnum.YELLOW + "Enter key: " + ColorEnum.FINISH)
            value = input(ColorEnum.YELLOW + "Enter value: " + ColorEnum.FINISH)
            hash_table.set_value(key, value)

        elif choice == '2':
            key = input(ColorEnum.YELLOW + "Enter key: " + ColorEnum.FINISH)
            if hash_table.del_value(key):
                print("\n" + ColorEnum.GREEN + "Happened" + ColorEnum.FINISH)
            else:
                print("\n" + ColorEnum.RED + "Value not found" + ColorEnum.FINISH)

        elif choice == '3':
            key = input(ColorEnum.YELLOW + "Enter key: " + ColorEnum.FINISH)
            value = hash_table.get_value(key)
            if value:
                print("\n" + value)
            else:
                print("\n" + ColorEnum.RED + "Value not found" + ColorEnum.FINISH)

        elif choice == '4':
            print("Table size:", hash_table.size, "\n")
            for i in range(hash_table.size):
                if hash_table.table[i]:
                    print("■", end="")
                else:
                    print("□", end="")
            print("\n" * 2 + "Fill factor: ", hash_table.load())

        elif choice == '5':
            print(hash_table)

        elif choice == '6':
            break

        else:
            print(ColorEnum.RED + "Incorrect choice. Try again" + ColorEnum.FINISH)


if __name__ == "__main__":
    main()
