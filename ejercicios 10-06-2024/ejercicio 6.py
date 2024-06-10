lista_producto=[]
def añadir_producto():
    añadir=input("Ingrese el producto que desea añadir: ")
    if añadir in lista_producto:
        lista_producto.append(añadir)
        print("Se ha agregado producto con exito")
    else:
        print("Se ha agregado producto con exito")
    print("Se ha ingresado el producto")

def mostrar_lista():
    print("===================")
    print("Lista de productos")
    for i, elementos in enumerate(lista_producto):
        print(f"{i+1}.-{elementos}")
    print("===================")

def menu():
    op=0
    while op!=3:
        try:
            print("Menu \n 1.-Añadir producto \n 2.-Mostrar lista de productos \n 3.-Salir")
            op=int(input("Seleccione una opcion: "))
            if op>3 or op<1:
                print("seleccione una opcion valida")
                continue
            else:
                if op==1:
                    añadir_producto()
                elif op==2:
                    mostrar_lista()
        except ValueError:
            print("Haz ingresado un caracter invalido")
            continue
menu()