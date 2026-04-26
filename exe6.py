a=int(input("Entrer un nombre: "))
if a == 1 or a == 0:
        print(f"{a} n'est ni pas premier")
else :
    for i in range(2, a):
        if a % i == 0:
            print(f"{a} n'est pas premier")
            break
    else:
        print(f"{a} est premier")

