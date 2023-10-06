def prosto(n):

    c = 0

    for i in range(1, int(n**0.5) + 1):
        if int(n) % i == 0:
            c += 1
            if c > 1:
                return False
    return True
        
x = int(input())

print(prosto(x))