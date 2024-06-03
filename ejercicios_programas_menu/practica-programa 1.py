from typing import Match 
contraseña="Abril2024" #se inicializa variable contraseña 

terminos=(input("Desea aceptar los terminos: (si/no)")).lower()
#Ciclo while verifica si los terminos son aceptados
while terminos!="si":
        terminos=(input("Debe aceptar los terminos para continuar: (si/no)")).lower()
        print("Error Ingrese una respuesta valida")

#variables que guardaron datos del usuario
nombre=(input("Ingrese su nombre: "))

correo=(input("Ingrese su correo: "))

#ciclo while para verificar que la contraseña sea correcta si no volver a pedirla
contraseña=str(input("Ingrese su contraseña: "))
while contraseña!="Abril2024":
    contraseña=str(input("Contraseña incorrecta vuelva a intentarlo: "))
#variable de opciones y total se inicializan
op=0
total=0
#ciclo while para el menu
while op!=3:
    print(" Menu \n1.Agregar compra \n2.Restar compra \n3.Salir")
    op=int(input("Seleccione una opcion: "))
   #Match para iniciar distintas secciones del codigo dependiendo de la opcion que escoga el usuario
    match op:
        case 1:
            agregar=float(input("Ingrese el valor a agregar: "))
            total=total+agregar
        case 2:
            restar=float(input("Ingrese el valor a restar: "))
            total=total-restar
        case 3:
            print(f"{nombre} el valor total de la compra es {total}")
            op=(input("Desea enviar el por correo electronico el pago? (si/no)")).lower()
            if op == "si":
                print(f"{correo} enviando pago")
                op=3
            if op=="no":
                print("Saliendo del programa...")
                op=3

         


    