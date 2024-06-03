bus=[[0]*4 for _ in range(10)]

asientos=1
for i in range(10):
    for j in range(4):
        bus[i][j]=asientos
        asientos+=1
for fila in bus:
    for columna in fila:
        print(columna,end="\t")
    print()
