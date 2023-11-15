from typing import List, Optional


class Hash:
    def __init__(self) -> None:
        self.size: int = 10
        self.fillinf: int = 0
        self.table: List[Optional[List[List[str]]]] = [None] * self.size

    def hash(self, key: str) -> int:
        result: int = sum(ord(c) for c in key) % self.size
        return result

    def set_value(self, key: str, value: str) -> None:
        hash_index: int = self.hash(key)
        if self.table[hash_index] is not None:
            for pair in self.table[hash_index]:
                if pair[0] == key:
                    pair[1] = value
                    return
            self.table[hash_index].append([key, value])
        else:
            self.table[hash_index] = [[key, value]]

    def get_value(self, key: str) -> Optional[str]:
        hash_index: int = self.hash(key)
        if self.table[hash_index] is not None:
            for pair in self.table[hash_index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def del_value(self, key: str) -> None:
        hash_index: int = self.hash(key)
        if self.table[hash_index] is None:
            return None
        for i in range(0, len(self.table[hash_index])):
            if self.table[hash_index][i][0] == key:
                self.table[hash_index].pop(i)
                if len(self.table[hash_index]) == 0:
                    self.table[hash_index] = None
                return

    def load(self) -> float:
        filled_buckets = len([bucket for bucket in self.table if bucket is not None])
        return filled_buckets / float(self.size)


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
