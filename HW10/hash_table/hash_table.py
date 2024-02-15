class HashTable:
    COLORS = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "finish": "\033[0m"
    }


    def __init__(self, size: int = 10):
        self.size = size
        self.table = self.init_table(size)

    def init_table(self, size: int) -> list:
        return [[] for _ in range(size)]

    def hash(self, key: str) -> int:
        return sum(ord(c) for c in key) % self.size

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
        hash_index: int = self.hash(key)
        for pair in self.table[hash_index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[hash_index].append([key, value])

    def get_value(self, key: str) -> str | None:
        hash_index: int = self.hash(key)
        for k, v in self.table[hash_index]:
            if k == key:
                return v
        return None

    def del_value(self, key: str) -> None:
        hash_index: int = self.hash(key)
        for i in range(0, len(self.table[hash_index])):
            if self.table[hash_index][i][0] == key:
                self.table[hash_index].pop(i)
                return True
        return False

    def load(self) -> float:
        return len([bucket for bucket in self.table if bucket]) / self.size

    def __str__(self) -> str:
        elements = [item for sublist in self.table for item in sublist if item]
        str_output = '{' + ', '.join('"{}": "{}"'.format(k, v) for k, v in elements) + '}'
        return str_output
