print("Menu")
op=0
total=0
registro=False
import getpass
while op!=3:
    try:
        print(" 1.-Registrar usuario \n 2.- Iniciar suma \n 3.-Salir")
        op=int(input("seleccione una opcion: "))
        if op>3 or op<0:
            print("seleccione una opcion valida")
    except:
        print("caracter invalido")
    from typing import Match
    match op:
        case 1:
            print("Registro")
            usuario=input("crea tu nombre de usuario: ")
            contraseña=getpass.getpass("Cree una contraseña: ")
            print("usuario y contraseña creada")
            registro=True
        case 2:
            if registro==True:
                print("iniciando sesion")
                while True:
                    user=input("Ingrese su nombre de usuario: ")
                    if user!=usuario:
                        print("el nombre de usuario es incorrecto")
                        continue
                    else:
                        break
                while True:
                    password=input("ingrese su contraseña: ")
                    if password!=contraseña:
                        print("la contraseña es incorrecta")
                        continue
                    else:
                        break
                while True:
                    try:
                        can_num=int(input("Ingrese cuantos numeros deseas sumar: "))
                        if can_num<0:
                            print("ingrese una cantidad valida")
                            continue
                        else:
                            break
                    except:
                        print("caracter invalido")
            else:
                print("debes registrarte primero")
                continue
            for i in range(can_num):
                suma=int(input("ingrese el numero a sumar: "))
                total=total+suma
        case 3:
            print(f"el valor total de la suma es {total}")
            
          

    
