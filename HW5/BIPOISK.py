def binary_search(sequence, target):
    low, high = 0, len(sequence)
    while low < high:
        mid = (low + high) // 2
        if sequence[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low if low < len(sequence) and sequence[low] == target else None


if __name__ == '__main__':
    g = [5, 3, 8, 3, 8, 9, 2, 7, 4, 0, 4, 3, 6, 6, 54534534, 635645]
    b = [1, 2, 3, 4, 5]


    print(binary_search([0, 1, 544444], 1))
