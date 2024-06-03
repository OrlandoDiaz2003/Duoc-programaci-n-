op=0
Biblioteca={
    "libro":[],
    "autor":[]
}
while op!=4:
    try:
        print("====================")
        print("Menu Biblioteca \n 1.-Añadir libro \n 2.-Buscar libro \n 3.-Eliminar libro \n 4.-Salir")
        op=int(input("Seleccione una opcion: "))
        if op>4 or op<1:
            print("Seleccione una opcion valida")
            continue
    except:
        print("Haz ingresado un caracter invalido")
    

    if op==1:
        print("====================")
        print("Añadir Libro")
        añadir_libro=input("Ingrese el nombre del libro: ").lower()
        añadir_autor=input("Ingrese su autor: ").lower()
        if añadir_libro not in Biblioteca:
            Biblioteca["libro"].append(añadir_libro)
            Biblioteca["autor"].append(añadir_autor)
            print("Se ha agregado el libro")
        else:
            print("Se ha agregdo el libro")
    elif op==2:
        print("====================")
        print("Buscar Libro")
        while True:
            buscar_libro=input("Ingrese el nombre del libro que deseas buscar: ").lower()
            if buscar_libro not in Biblioteca["libro"]:
                print("Este libro no se encuentra en la biblioteca")
                break
            else:
                libro_selec=Biblioteca["libro"].index(buscar_libro)
                print(f"Aqui esta el libro que buscas {Biblioteca['libro'][libro_selec].title()} escrito por {Biblioteca['autor'][libro_selec].title()}")
                break 
    elif op==3:
        print("====================")
        print("Eliminar libro")
        while True:
            eliminar_libro=input("Ingrese el nombre del libro que desea eliminar: ")
            if eliminar_libro not in Biblioteca["libro"]:
                print("Este libro no se encuentra  en la biblioteca")
                break
            else:
                libro_selec=Biblioteca["libro"].index(eliminar_libro)
                print(f"El libro eliminado {Biblioteca['libro'][libro_selec]} escrito por {Biblioteca['autor'][libro_selec]}") 
                autor_eliminar=Biblioteca["autor"][libro_selec]
                Biblioteca["autor"].remove(autor_eliminar)
                Biblioteca["libro"].remove(eliminar_libro)
                break