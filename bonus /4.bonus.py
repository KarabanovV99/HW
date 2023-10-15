def extract_ranges(numbers: list) -> str:
    result = []
    i = 0
    while i < len(numbers):
        start = numbers[i]
        end = start
        while i + 1 < len(numbers) and numbers[i+1] == end + 1:
            i += 1
            end = numbers[i]
        if end - start >= 2:
            result.append(f"{start}-{end}")
        else:
            result.extend(str(num) for num in range(start, end + 1))
        i += 1
    return ", ".join(result)


print(extract_ranges([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))

print(extract_ranges([12, 13, 15, 16, 17]))
