import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    sorted_numbers = quick_sort(numbers)
    print(sorted_numbers)
