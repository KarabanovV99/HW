from typing import List, Optional

size: int = 10
fillinf: int = 0
table: List[Optional[List[List[str]]]] = [None] * size

def hash(key: str) -> int:
    result: int = sum(ord(c) for c in key) % size
    return result

def set_value(key: str, value: str) -> None:
    hash_index: int = hash(key)
    if table[hash_index] is not None:
        for pair in table[hash_index]:
            if pair[0] == key:
                pair[1] = value
                return
        table[hash_index].append([key, value])
    else:
        table[hash_index] = [[key, value]]

def get_value(key: str) -> Optional[str]:
    hash_index: int = hash(key)
    if table[hash_index] is not None:
        for pair in table[hash_index]:
            if pair[0] == key:
                return pair[1]
    return None

def del_value(key: str) -> None:
    hash_index: int = hash(key)
    if table[hash_index] is None:
        return None
    for i in range(0, len(table[hash_index])):
        if table[hash_index][i][0] == key:
            table[hash_index].pop(i)
            if len(table[hash_index]) == 0:
                table[hash_index] = None
            return

def load() -> float:
    filled_buckets = len([bucket for bucket in table if bucket is not None])
    fill_ratio = filled_buckets / float(size)
    for i in range(size):
        if table[i] is not None:
            print('\u25A0', end="")
        else:
            print('\u25A1', end="")
    print()

    return fill_ratio
