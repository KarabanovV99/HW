c1 = 1
c2 = 1

n = int(input())

print(c1)
if n >= 2:
    print(c2)
 
for i in range(2, n):
    c1, c2 = c2, c1 + c2
    print(c2)