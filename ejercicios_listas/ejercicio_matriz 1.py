matriz=[
    [],
    [],
    [],
]

fila=0
while fila!=3:
    print(f"Ingresa valores a la fila {fila+1}")
    for i in range(4):
        while True:
            try:
                agregar_fila=int(input("Agrege un valor: "))
                break
            except:
                print("haz ingresado un carater invalido")
                continue
        matriz[fila].append(agregar_fila)
    fila+=1

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()