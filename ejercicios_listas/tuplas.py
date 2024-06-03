mi_tupla = (1,"dos",3.0)
mi_lista=[1,"dos",3.0]

#convertir lista en tupla
mi_lista2=[1,2,3]
mi_tupla2= tuple(mi_lista2)
print(mi_tupla2)

#diccionarios
diccionario = {"nombre": "Cesar Huispe",
"fonos": [
988778882,
988877776,
877666333],
"activo": True}
print(diccionario["nombre"]) #imprimir dato de diccionario
diccionario["direccion"]="viña" #agregar datos a diccionario
print(diccionario["direccion"])
del diccionario["direccion"] #Eliminar datos del diccionario
print(diccionario["direccion"])



#conjuntos (set)
conjunto = {3, 1, 4, 1, 5, 2, 4}
lista = [3, 1, 4, 1, 5, 2, 4]
print ("Conjunto")
print(conjunto)
print ("Lista")
print(lista)