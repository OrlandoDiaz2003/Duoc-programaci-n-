#matriz_sencilla = [
#    [1, 2, 3],
#    [4, 5, 6]
#]
#for elemento in matriz_sencilla:
#    print(elemento)

#print(matriz_sencilla[0][2])

#for fila in matriz_sencilla:
#    for elemento in fila:
#        print(elemento, end=" ")
#    print()

arreglo_3D=[
    [
        [1,2,3],
        [4,5,6],

    ],
    [
        [7,8,9],
        [10,11,12],
    ],
    [
        [13,14,15],
        [16,17,18],
    ]
]

for dimension in arreglo_3D:
    for fila in dimension:
        for numero in fila:
            print(numero, end= " ")
        print()
    print()