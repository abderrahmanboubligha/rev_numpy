somme = 0
for i in range(1, 20):
    if i % 2 == 0:
        continue
    somme += i
print(f"La somme est : {somme}")