lista=[]
nombre_mayor=0
for i in range(3):
    nombre=input(f"Ingrese nombre nombre {i+1}: ")
    lista.append(nombre)
for caracter in lista:
    cantidad=len(caracter)
    if cantidad>nombre_mayor:
        nombre_mayor=cantidad
        posicion=lista.index(caracter)

print(lista[posicion])
