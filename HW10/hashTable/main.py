class HashTable:
    COLORS = {
        "red": "\033[31m",
        "finish": "\033[0m",
        "green": "\033[32m",
        "yellow": "\033[33m",
    }

    def __init__(self, size: int):
        self.size = size
        self.table = self.init_table(size)

    def init_table(self, size: int) -> list:
        return [[] for _ in range(size)]

    @staticmethod
    def hashing(key: str, size: int) -> int:
        return sum(ord(c) for c in key) % size

    def resize(self) -> None:
        old_table = self.table
        self.size *= 2
        self.table = self.init_table(self.size)
        for bucket in old_table:
            for key, value in bucket:
                self.set_value(key, value)

    def set_value(self, key: str, value: str) -> None:
        load_factor = self.load()
        if load_factor > 0.75:
            self.resize()
        hash_index: int = self.hashing(key, self.size)
        for pair in self.table[hash_index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[hash_index].append([key, value])

    def get_value(self, key: str) -> str | None:
        hash_index: int = self.hashing(key, self.size)
        for k, v in self.table[hash_index]:
            if k == key:
                return v
        return None

    def del_value(self, key: str) -> None:
        hash_index: int = self.hashing(key, self.size)
        for i in range(0, len(self.table[hash_index])):
            if self.table[hash_index][i][0] == key:
                self.table[hash_index].pop(i)
                return

    def load(self) -> float:
        return len([bucket for bucket in self.table if bucket]) / self.size

    def __str__(self) -> str:
        elements = [item for sublist in self.table for item in sublist if item]
        str_output = '{' + ', '.join('"{}": "{}"'.format(k, v) for k, v in elements) + '}'
        return str_output


def main():
    size: int = 3
    hash_table = HashTable(size)
    while True:
        print(HashTable.COLORS["red"] + "1. Добавить значение")
        print("2. Удалить значение")
        print("3. Получить значение")
        print("4. Коэффициент заполнения")
        print("5. Вывести таблицу")
        print("6. Выход" + HashTable.COLORS["finish"])

        choice = input(HashTable.COLORS["green"] + "Введите ваш выбор: " + HashTable.COLORS["finish"])

        if choice == '1':
            key = input(HashTable.COLORS["green"] + "Введите ключ: " + HashTable.COLORS["finish"])
            value = input(HashTable.COLORS["green"] + "Введите значение: " + HashTable.COLORS["finish"])
            hash_table.set_value(key, value)

        elif choice == '2':
            key = input(HashTable.COLORS["green"] + "Введите ключ: " + HashTable.COLORS["finish"])
            hash_table.del_value(key)

        elif choice == '3':
            key = input(HashTable.COLORS["green"] + "Введите ключ: " + HashTable.COLORS["finish"])
            value = hash_table.get_value(key)
            if value:
                print(value)
            else:
                print(HashTable.COLORS["yellow"] + "Значение не найдено." + HashTable.COLORS["finish"])

        elif choice == '4':
            print("Table size:", hash_table.size)
            for i in range(hash_table.size):
                if hash_table.table[i]:
                    print("■", end="")
                else:
                    print("□", end="")
            print("\n", "Коэффициент заполнения:", hash_table.load())

        elif choice == '5':
            print(hash_table)

        elif choice == '6':
            break

        else:
            print(HashTable.COLORS["yellow"] + "Неверный выбор. Попробуйте еще раз." + HashTable.COLORS["finish"])


if __name__ == "__main__":
    main()
