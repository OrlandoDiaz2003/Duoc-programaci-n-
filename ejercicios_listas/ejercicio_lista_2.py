nombres=[]
apellidos=[]
posicion=0
for i in range(3):
    agregar_nombres=input("Ingrese un nombre a la lista: ")
    nombres.append(agregar_nombres)
    agregar_apellido=input("Ingrese un apellido a la lista: ")
    apellidos.append(agregar_apellido)
print("Nombres Apellidos")
for i in range(3):
    print(nombres[posicion], apellidos[posicion])
    posicion=posicion+1
