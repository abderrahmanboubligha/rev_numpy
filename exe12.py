def exe12 (n):
    if n == 0 :
        return 2
    elif n == 1 :
        return 3
    else :
        return 2/3*exe12(n-1) - 1/4*exe12(n-2)
    
def exe12_clasic (n):
    if n < 2 : 
        return 2 + n
    else :
        a = 2
        b = 3
        for i in range(2, n+1):
            c = 2/3*b - 1/4*a
            a, b = b, c
        return c


def exe13 (n):
    if n < 3 :
        return n
    else :
        return exe13(n-1) + exe13(n-3)
def exe13_classic (n):
    if n < 3 :
        return n
    else :
        a = 0
        b = 1
        c = 2
        for i in range(3, n+1):
            d = c + a
            a, b, c = b, c, d
        return d

exe13(10)

