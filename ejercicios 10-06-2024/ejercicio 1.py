nombres=[]
apellidos=[]
def nombre_apellido():
    nombre=input("Ingrese su nombre: ")
    apellido= input("Ingrese su apellido: ")
    print("se han ingresado correctamente")
    nombres.append(nombre)
    apellidos.append(apellido)

def buscar_nombre():
    while True:
        buscar=input("Ingrese el nombre que deseas buscar: ")
        if buscar not in nombres:
            print("El nombre ingresado no se encuentra en la lista")
            continue
        else:
            posicion=nombres.index(buscar)
            print(f"El nombre que buscas es {nombres[posicion]} {apellidos[posicion]}")
            break   
nombre_apellido()

buscar_nombre()