from enum import StrEnum


class ColorEnum(StrEnum):
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    FINISH = "\033[0m"


class HashTable:
    def __init__(self, size: int = 10, dict_mode: None | dict = None):
        if dict_mode is not None:
            if not isinstance(dict_mode, dict):
                raise TypeError(ColorEnum.RED + 'Вы подали не словарь, а какую-то *****' + ColorEnum.FINISH)
            self.size = size
            self.table = self.init_table(size)
            self.dict_to_hesh(dict_mode)
        else:
            self.size = size
            self.table = self.init_table(size)

    @staticmethod
    def init_table(size: int) -> list:
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

    def del_value(self, key: str) -> bool:
        hash_index: int = self.hash(key)
        for i in range(0, len(self.table[hash_index])):
            if self.table[hash_index][i][0] == key:
                self.table[hash_index].pop(i)
                return True
        return False

    def load(self) -> float:
        return len([bucket for bucket in self.table if bucket]) / self.size

    def dict_to_hesh(self, dic: dict) -> None:
        for key, value in dic.items():
            self.set_value(key, value)

    def __str__(self) -> str:
        elements = [item for sublist in self.table for item in sublist if item]
        str_output = '{' + ', '.join('"{}": "{}"'.format(k, v) for k, v in elements) + '}'
        return str_output


if __name__ == '__main__':
    d = {'персона': 'человек',
         'марафон': 'гонка бегунов длиной около 26 миль',
         'противостоять': 'оставаться сильным, несмотря на давление',
         'бежать': 'двигаться со скоростью'}
    hash_table = HashTable(len(d), d)
    print(hash_table)
