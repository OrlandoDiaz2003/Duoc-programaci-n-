from typing import Match
op=0
Lista_nombres=[]
Lista_contraseña=[]
registro=False
while op!=4:
    print(" 1.-Inicio de sesion \n 2.-Registrar usuario \n 3.-Eliminir usuario \n 4.-Salir")
    try:
        op=int(input("Seleccione una opcion: "))
        if op<1 or op>4:
            print("Seleccione una opcion valida")
    except:
        print("Haz ingresado una caracter invalido")
        continue
    match op:
        case 1:
            if registro==False:
                print("No tienes usuarios registrados")
            else:
                while True:
                    print("Inicio de sesion")
                    usuario=input("Ingrese su usuario: ")
                    if usuario in Lista_nombres:
                        Posicion=Lista_nombres.index(usuario)
                        break
                    else:
                        print("El usuario ingresado no existe")
                        
                while True:
                    contraseña=input("Ingrese su contraseña: ")
                    if contraseña==Lista_contraseña[Posicion]:
                        print("Haz Ingresado con exito")
                        break
                    else:
                        print("Contraseña incorrecta")
                    
        case 2:
            print("Registro de usuario")
            usuario=input("Crea tu nombre de usuario: ")
            Lista_nombres.append(usuario)
            contraseña=input("Crea tu contraseña: ")
            Lista_contraseña.append(contraseña)
            print("Usuario creado con exito")
            registro=True
        
        case 3:
            if registro==False:
                print("No existe ningun usuario")
            else:
                while True:
                    print("Eliminacion de usuario")
                    usuario=input("Ingrese el usuario que desea eliminar: ")
                    if usuario in Lista_nombres:
                        Posicion=Lista_nombres.index(usuario)
                        break
                    else:
                        print("El usuario ingresado no existe")
                        continue
                while True:
                    contraseña=input("Ingrese la contraseña del usuario para confirmar eliminacion: ")
                    if contraseña==Lista_contraseña[Posicion]:
                        print(f"Eliminando usuario {Lista_nombres[Posicion]}")
                        Lista_nombres.remove(usuario)
                        Lista_contraseña.remove(contraseña)

        