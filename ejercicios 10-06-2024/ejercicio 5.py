contactos={}

def añadir_contacto(): 
    nombre=input("Ingrese el nombre del usuario: ")
    while True:
        try:
            numero=int(input("Ingrese el numero del contacto: "))
            break
        except ValueError:
            print("Haz ingresado un numero invalido")
            continue
    contactos[nombre]=numero
    print(contactos)

def buscar_contacto():
    while True:
        buscar=input("Ingrese el usuario que deseas buscar: ")
        if buscar not in contactos:
            print("El usuario no existe vuelva a intentarlo")
        else:
            print(f"Nombre: {buscar} \nnumero: {contactos[buscar]}")
            break

def menu():
    op=0
    while op!=3:
        print("Menu \n 1.-Añadir contacto \n 2.-Buscar contacto \n 3.-Salir")
        op=int(input("Seleccione una opcion: "))
        if op>3 or op<0:
            print("ingrese una opcion valida")
        else:
            if op==1:
                añadir_contacto()
            elif op==2:
                buscar_contacto()

menu()