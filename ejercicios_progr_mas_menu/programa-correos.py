op=0
op2=0
usuario1=0
usuario2=0
usuario3=0
contraseña1=0
contraseña2=0
contraseña3=0
user=0
password=0
registro=False
while op!=3:
    print("==========================")
    print("Menu \n 1.-Iniciar sesion \n 2.-Registrar usuario \n 3.-Salir")
    print("==========================")
    op2=0
    try:
        op=int(input("Seleccione una opcion: "))
        if op>3 or op<1:
            print("Error ingrese una opcion valida")
            continue
    except:
        print("Error ingrese una opcion valida")
        continue
    if op==1:
        if registro==False:
            print("Debes registrar un usuario primero")
            continue
        else:
            print("Iniciando sesion")
            while True:
                user=input("Ingrese un usuario: ")
                if user!=usuario1 and user!=usuario2 and user!=usuario3:
                    print("Ingrese un usuario valido")
                    continue
                if user==usuario1:
                    while True:
                        password=input("Ingrese su contraseña: ")
                        if password!=contraseña1:
                            print("Contraseña incorrecta")
                        else:
                            print("Iniciando sesion")
                            break
                            
                elif user==usuario2:
                    while True:
                        password=input("Ingrese su contraseña: ")
                        if password!=contraseña2:
                            print("Contraseña incorrecta")
                        else:
                            print("Iniciando sesion")
                            break
                    
                elif user==usuario3:
                    while True:
                        password=input("Ingrese su contraseña: ")
                        if password!=contraseña3:
                            print("Contraseña incorrecta")
                        else:
                            print("Iniciando sesion")
                            break
                break
        while op2!=3:
            try:
                print("==========================")
                print(f"Bienvenido {user}")
                print("1.-Realizar llamada \n2.-Enviar correo electronico \n3.-Cerrar sesion")
                print("==========================")
                op2=int(input("Seleccione una opcion: "))
                if op2>3 or op<=0:
                    print("Ingrese una opcion valida")
                    continue
            except:
                print("haz ingresado un caracter invalido")
            if op2==1:
                while True:
                    try:
                        numero=input("Ingrese un numero de telefono (recuerde agregar el 9 al principio): ")
                        numero=numero.strip()
                        if numero[0]=="9" and len(numero)==9:
                            numero=int(numero)
                            print("Llamada realizada con exito")
                            numero=str(numero)
                            break
                        else:
                            print("ingrese un numero valido")

                    except:
                        print("Error, haz ingresado un caracter invalido")
                        continue

            elif op2==2:
                while True:
                    correo=input("Ingrese correo electronico: ")
                    if "@" in correo and ".com" in correo:
                        print("correo Ingresado con exito")
                        mensaje=input("Escriba su mensaje \n: ")
                        break
                    else:
                        print("ingrese un correo valido ejemplo (usuario@gmail.com)")
                        continue
            elif op2==3:
                print(f"Cerrando sesion adios {user}")
                break   
                    

    elif op==2:
        if usuario1==0:
            print("usuario 1")
            usuario1=(input("Ingrese un usuario: "))
            contraseña1=(input("Ingrese una contraseña: "))
            registro=True
            print("usuario creado")
            continue
        else:
            if usuario2==0:
                print("usuario 2")
                usuario2=(input("Ingrese un usuario: "))
                contraseña2=(input("Ingrese una contraseña: "))
                print("usuario creado")
                continue
            else:
                if usuario3==0:
                    print("usuario 3")
                    usuario3=(input("Ingrese un usuario: "))
                    contraseña3=(input("Ingrese una contraseña: "))
                    print("usuario creado")
                    continue
                else:
                    print("todos los usuarios han sido creados")
                    continue

        

        
    