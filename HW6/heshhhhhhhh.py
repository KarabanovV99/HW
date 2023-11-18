COLORS = {
    "red": "\033[31m",
    "finish": "\033[0m",
    "green": "\033[32m",
    "yellow": "\033[33m",
}


def init_table(size: int) -> list:
    return [[] for _ in range(size)]


def hashing(key: str, size: int) -> int:
    return (sum(ord(c) for c in key)) % size


def resize(size: int, table: list) -> int | list:
    old_table = table
    size *= 2
    table = init_table(size)
    for bucket in old_table:
        for key, value in bucket:
            size, table = set_value(key, value, table, size)
    return size, table


def set_value(key: str, value: str, table: list, size: int) -> list:
    load_factor = load(table)
    if load_factor > 0.75:
        size, table = resize(size, table)
    hash_index: int = hashing(key, size)
    for pair in table[hash_index]:
        if pair[0] == key:
            pair[1] = value
            return
    table[hash_index].append([key, value])
    return size, table


def get_value(key: str, table: list, size: int) -> str | None:
    hash_index: int = hashing(key, size)
    for k, v in table[hash_index]:
        if k == key:
            return v
    return


def del_value(key: str, table: list, size: int) -> list:
    hash_index: int = hashing(key, size)
    for i in range(0, len(table[hash_index])):
        if table[hash_index][i][0] == key:
            table[hash_index].pop(i)
            return table


def load(table) -> float:
    return len([bucket for bucket in table if bucket]) / len(table)
