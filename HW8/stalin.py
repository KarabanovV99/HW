def stalin_sort(arr):
    if len(arr) == 0:
        return arr
    else:
        sorted_arr = [arr[0]]
        for i in range(1, len(arr)):
            if arr[i] >= sorted_arr[-1]:
                sorted_arr.append(arr[i])
        return sorted_arr


if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    sorted_numbers = stalin_sort(numbers)
    print(sorted_numbers)
