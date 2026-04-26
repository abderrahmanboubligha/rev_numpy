### Chapter 3
l=[[1 if i == j else 0 for j in range(3)] for i in range(3)]
print(l)


L=[[1, 2], [3,4], [5,6]]
l2=[el for ligne in L for el in ligne]
#whit indexes now
l3=[L[i][j] for i in range(len(L)) for j in range(len(L[i]))]
print(l2)
print(l3)

#multiplication,of 1to 5 sous list
L=[[i*j for j in range(1,6)] for i in range(1,6)]
print(L)
#i want to show 1,1 table 1,2 table 1,3 table then 2,1 table 2,2 table 2,3 table etc

L=[(i, j) for i in range(1,4) for j in range(1,4)]
print(L)

L=["banana", "pomme", "cerise"]
L=[el[0] for el in L]
print(L)