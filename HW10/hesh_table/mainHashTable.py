from heshTable import HashTable


def main():
    size: int = 10
    hash_table = HashTable(size)
    while True:
        print(HashTable.COLORS["blue"] + "_" * 27 + HashTable.COLORS["finish"], "\n")
        print(HashTable.COLORS["green"] + "1. Add value")
        print("2. Delete value")
        print("3. Get value")
        print("4. Fill factor")
        print("5. Print dictionary")
        print("6. Exit" + HashTable.COLORS["finish"], "\n")

        choice = input(HashTable.COLORS["yellow"] + "Enter your choice: " + HashTable.COLORS["finish"])
        print("")

        if choice == '1':
            key = input(HashTable.COLORS["yellow"] + "Enter key: " + HashTable.COLORS["finish"])
            value = input(HashTable.COLORS["yellow"] + "Enter value: " + HashTable.COLORS["finish"])
            hash_table.set_value(key, value)

        elif choice == '2':
            key = input(HashTable.COLORS["yellow"] + "Enter key: " + HashTable.COLORS["finish"])
            if hash_table.del_value(key):
                print("\n" + HashTable.COLORS["green"] + "Happened" + HashTable.COLORS["finish"])
            else:
                print("\n" + HashTable.COLORS["red"] + "Value not found" + HashTable.COLORS["finish"])

        elif choice == '3':
            key = input(HashTable.COLORS["yellow"] + "Enter key: " + HashTable.COLORS["finish"])
            value = hash_table.get_value(key)
            if value:
                print("\n" + value)
            else:
                print("\n" + HashTable.COLORS["red"] + "Value not found" + HashTable.COLORS["finish"])

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
            print(HashTable.COLORS["red"] + "Incorrect choice. Try again" + HashTable.COLORS["finish"])


if __name__ == "__main__":
    main()
