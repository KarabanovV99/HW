lst = []
while True:
    n = input()
    if n == "":
        break
    lst.append(n)
m = int(input())
lst1 = [''.join(map(str, lst))]
f = str(lst1)
print(f[m + 1])
