stock={
    "carne":{"cantidad":10, "precio":10000},
    "carne mediana":{"cantidad":9, "precio":10000},
    "carne grande":{"cantidad":8, "precio":10000}

}
def añadir_producto():
    producto=input("Ingrese el nombre del producto: ")
    while True:
        try:
            cantidad=int(input("Ingrese la cantidad: "))
            if cantidad<1:
                print("Ingrese una cantidad valida")
                continue
            else:
                break
        except ValueError:
            print("Haz ingresado un carcter invalido")
    while True:
        try:
            precio=int(input("Ingrese el precio del producto: "))
            if precio<1:
                print("Ingrese un valor valido")
                continue
            else:
                break
        except ValueError:
            print("Haz ingresado un caracter invalido")

    stock[producto]={"cantidad":cantidad, "precio":precio}

def eliminar_producto():
    while True:
        buscar=input("Ingrese el producto que desea eliminar: ")
        if buscar not in stock:
            print("Este producto no existe")
            continue
        else:
            print(stock[buscar])
            del stock[buscar]
            break

def actualizar_cantidad():
    for i,elemento in enumerate(stock):
        print(f"{i+1}.-{elemento}")
    
    while True:
        try:
            rsp=int(input("Seleccione algun producto: "))
            if rsp<1 or rsp>(i+1):
                print("Seleccione una opcion valida")
                continue
            else:
                buscar_producto=list(stock.keys())[rsp-1]
                print(f"Haz seleccionado \n producto: {buscar_producto} \n cantidad: {stock[buscar_producto]["cantidad"]}")
                break
        except ValueError:
            print("Haz ingresado un caracter invalido")
            continue
    while True:
        try:
            cantidad=int(input("Actualize la cantidad disponible de este producto: "))
            if cantidad<0:
                print("No puedes actualizar la cantidad a menos de 0")
                continue
            else:
                stock[buscar_producto]["cantidad"]=cantidad
                print(f"Haz Actualizado la cantidad \n producto: {buscar_producto} \n cantidad: {stock[buscar_producto]["cantidad"]}")
                break
        except ValueError:
            print("Haz ingresado un  caracter invalido")
            continue

def mostrar_inventario():
    for i,productos in enumerate(stock):
        print(f"{i+1}.-{productos}: cantidad: {stock[productos]["cantidad"]} precio: {stock[productos]["precio"]}$")

def buscar_productos():
    while True:
        buscar=input("Ingrese el producto del que desea ver informacion: ")
        if buscar not in stock:
            print("El producto que haz ingresado no se encuentra en el stock vuelva a intentarlo")
            continue
        else:
            print(f"Producto: {buscar} \nCantidad: {stock[buscar]["cantidad"]} \nPrecio: {stock[buscar]["precio"]} $")
            break

def menu():
    op=0
    while op!=6:
        try:
            print("=====================")
            print("Menu \n 1.-Añadir producto \n 2.-Eliminar producto \n 3.-Actualizar cantidad \n 4.-Mostrar inventario \n 5.-Buscar Producto \n 6.-Salir")
            print("=====================")
            op=int(input("Seleccione una opcion: "))
            if op>6 or op<1:
                print("Ingrese una opcion valida")
            else:
                if op==1:
                    añadir_producto()
                elif op==2:
                    eliminar_producto()
                elif op==3:
                    actualizar_cantidad()
                elif op==4:
                    mostrar_inventario()
                elif op==5:
                    buscar_productos()
        except ValueError:
            print("Haz ingresado un caracter invalido")

menu()