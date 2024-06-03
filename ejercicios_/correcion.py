print("Correo")
op = 0
op2 = 0
usuario1 = 0
usuario2 = 0
usuario3 = 0
contraseña1 = 0
contraseña2 = 0
contraseña3 = 0
user = 0
password = 0
registro = False
inicio = False

while op != 3:
    print("==========================")
    print("Menu \n 1.-Iniciar sesion \n 2.-Registrar usuario \n 3.-Salir")
    print("==========================")
    inicio = False  # Reinicia la variable inicio en cada iteración del ciclo principal
    try:
        op = int(input("Seleccione una opcion: "))
        if op > 3 or op < 1:
            print("Error ingrese una opcion valida")
    except:
        print("Error ingrese una opcion valida")
    if op == 1:
        if registro == False:
            print("Debes registrar un usuario primero")
            continue
        else:
            print("Iniciando sesion")
            while inicio == False:
                user = input("Ingrese un usuario: ")
                if user != usuario1 and user != usuario2 and user != usuario3:
                    print("Ingrese un usuario valido")
                    continue
                if user == usuario1:
                    while True:
                        password = input("Ingrese su contraseña: ")
                        if password != contraseña1:
                            print("Contraseña incorrecta")
                        else:
                            print("Iniciando sesion")
                            inicio = True
                            break
                elif user == usuario2:
                    while True:
                        password = input("Ingrese su contraseña: ")
                        if password != contraseña2:
                            print("Contraseña incorrecta")
                        else:
                            print("Iniciando sesion")
                            inicio = True
                            break
                elif user == usuario3:
                    while True:
                        password = input("Ingrese su contraseña: ")
                        if password != contraseña3:
                            print("Contraseña incorrecta")
                        else:
                            print("Iniciando sesion")
                            inicio = True
                            break
        while op2 != 3:
            try:
                print("==========================")
                print(f"Bienvenido {user}")
                print("1.-Realizar llamada \n2.-Enviar correo electronico \n3.-Cerrar sesion")
                print("==========================")
                op2 = int(input("Seleccione una opcion: "))
                if op2 > 3 or op2 < 1:  # <-- Aquí debería ser op2, no op
                    print("Ingrese una opcion valida")
                    continue
            except:
                print("Haz ingresado un caracter invalido")
            if op2 == 1:
                while True:
                    try:
                        numero = input("Ingrese un numero de telefono (recuerde agregar el 9 al principio): ")
                        if numero[0] == "9" and len(numero) == 9:
                            numero = int(numero)
                            print("Llamada realizada con exito")
                            numero = str(numero)
                            break
                        else:
                            print("Ingrese un numero valido")

                    except:
                        print("Error, haz ingresado un caracter invalido")
                        continue

            elif op2 == 2:
                while True:
                    correo = input("Ingrese correo electronico: ")
                    if "@" in correo and ".com" in correo:
                        print("Correo ingresado con exito")
                        mensaje = input("Escriba su mensaje \n: ")
                        break
                    else:
                        print("Ingrese un correo valido ejemplo (usuario@gmail.com)")
                        continue
            elif op2 == 3:
                print(f"Cerrando sesion adios {user}")
                op = 0  # Reinicia op para que el bucle principal solicite una nueva entrada
                break

    elif op == 2:
        if usuario1 == 0:
            print("Usuario 1")
            usuario1 = input("Ingrese un usuario: ")
            contraseña1 = input("Ingrese una contraseña: ")
            registro = True
            print("Usuario creado")
            continue
        else:
            if usuario2 == 0:
                print("Usuario 2")
                usuario2 = input("Ingrese un usuario: ")
                contraseña2 = input("Ingrese una contraseña: ")
                print("Usuario creado")
                continue
            else:
                if usuario3 == 0:
                    print("Usuario 3")
                    usuario3 = input("Ingrese un usuario: ")
                    contraseña3 = input("Ingrese una contraseña: ")
                    print("Usuario creado")
                    continue
                else:
                    print("Todos los usuarios han sido creados")
                    continue
