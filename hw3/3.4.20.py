from collections import Counter
from one import vvod


def f(lst):
    return Counter(lst).most_common()


lst = vvod()
sorted_counter = f(lst)

output = ["Элемент | Частота"]

for e, c in sorted_counter:
    output.append(f"{e.ljust(7)} | {str(c).ljust(7)}")


print('\n'.join(output))
