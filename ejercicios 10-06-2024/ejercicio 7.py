biblioteca= {}
def añadir_libro():
    libro=input("Ingrese el libro a añadir: ").title()
    autor=input("Ingrese su autor: ").title()
    biblioteca[libro]=autor
    print("Se ingresado el libro correctamente")

def buscar_libro():
    while True:
        libro=input("Ingrese el libro que desea buscar: ").title()
        if libro not in biblioteca:
            print("Este libro no se encuentra en la biblioteca")
            continue
        else:
            print(f"el libro que buscas es \n Libro: {libro} \n Autor: {biblioteca[libro]}")
            break
def menu():
    op=0
    while op!=3:
        print("Menu Biblioteca \n 1.-Añadir libro \n 2.-Buscar libro \n 3.-Salir")
        op=int(input("Seleccione una opcion: "))
        if op>3 or op<1:
            print("Ingrese una opcion valida")
            continue
        else:
            if op==1:
                añadir_libro()
            elif op==2:
                buscar_libro()
menu()
