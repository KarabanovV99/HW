def prosto(n):

    c = 0

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            c += 1
            return False
    return True
        
x = int(input("Число: "))

print(prosto(x))