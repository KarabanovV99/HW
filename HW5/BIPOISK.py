def binary_search(sequence, target):
    low, high = 0, len(sequence) - 1
    result = None
    while low <= high:
        mid = (low + high) // 2
        if sequence[mid] >= target:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result
