from collections import Counter
from one import vvod


def f(lst):
    sorted_counter = Counter(lst).most_common()
    output = ["Элемент | Частота"]

    for e, c in sorted_counter:
        output.append(f"{e.ljust(7)} | {c:4}")

    return '\n'.join(output)




print(f(vvod()))
