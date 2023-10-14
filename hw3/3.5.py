def sr_sum(n):
    return sum(n) / len(n)


lst = [int(n) for n in input().split()]

print(sr_sum(lst))
