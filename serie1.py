n= int(input("Entrez un nombre: "))
somme = 0
for i in range(1, n*2, 2):
    somme += i**2
print(f"La somme des carrés des {n} premiers nombres impairs est: {somme}")




