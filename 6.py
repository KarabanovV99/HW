# lst = []
# lst2 = []

# while True:
#     n = input()
#     if not n:
#         break
#     lst.append(n)

# m = int(input())
# lst1 = [''.join(lst)]
# # lst1 = [''.join(map(str, lst))]
# # y = input()
# #y = lst1[0]
# for x in y:
#     # if x in '1234567890':
#     if x.isdigit():
#         lst2.append(x)
# print(lst2[m - 1])

x = input()
y = y0 = int(input())
a = 0
for i in x:
    if i.isdigit():
        y -= 1
        if not y:
            print(y0, "-ая цифра в строке:", i)
            break
