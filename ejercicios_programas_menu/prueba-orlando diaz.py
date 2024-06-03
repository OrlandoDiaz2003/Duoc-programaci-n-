op=0
peso_total=0
precio_total=0
pesoagregado=False #variable booleana que valida si agrego equipaje 
pago=False
edad_registro=False #Variable booleana que valida si el usuario ingreso su edad, si este ya la ingreso y desea volver agregar equipaje no se la volvera a pedir
while op!=3: #Bucle que inicia el menu principal
    print("====================")
    print("Aerolinea TAMLA")
    print("Menu Principal \n 1.-Ingresar Check-in \n 2.-Pagar Check-in \n 3.-Salir")
    print("====================")
    try:
        op=int(input("Seleccion una opcion: "))
        if op<0 or op>3:
            print("Ingrese una opcion valida")
    except:
        print("Haz ingresado un caracter invalido use (1,2,3)")
    #Ingresar al submenu
    if op==1:
        op2=0 #al ingresar al submenu se inicia la variable op2 en 0 (no la agrege arriba para que cuando salga y entre de este menu la variable se reinicie y vuelva a 0)
        print("Ingresando al menu")
        while op2!=3:
            try:
                print("====================")
                print("Submenu \n 1.-Agregar Equipaje \n 2.-Restar Equipaje \n 3.-Volver al menu")
                print("====================")
            
                op2=int(input("Seleccione una opcion: "))
                if op2<0 or op2>3:
                    print("Seleccione una opcion valida")
            except:
                print("Haz ingresado un caracter invalido use (1,2,3)")
            
            #Agregar equipaje
            
            if op2==1:
                while True:
                    try:
                        if edad_registro==False:
                            edad=int(input("Ingrese su edad: "))
                            if edad<0:
                                print("Edad invalida, vuelvalo a intentar")
                            else:
                                edad_registro=True
                                break
                        else:
                            break
                    except:
                        print("Edad invalidad ingrese su edad (ejemplo: 20)")

                while True:
                    try:
                        equip_abast=int(input("Ingresa la cantidad de equipo que va a agregar: "))
                        if equip_abast<0:
                            print("Ingrese una cantidad valida")
                    except:
                        print("Ingresa una cantidad valida (ejemplo: 3)")
                    for i in range(equip_abast):
                        try:
                            equip_peso=int(input("Ingrese el peso del equipaje (min: 10kg): "))
                            if equip_peso<10:
                                print("Ingrese un peso valido")
                            elif 20>equip_peso>=10:
                                peso_total=peso_total+equip_peso
                                precio_total=precio_total+10000
                            elif 20<=equip_peso<30:
                                peso_total=peso_total+equip_peso
                                precio_total=precio_total+20000
                            elif equip_peso>=30:
                                peso_total=peso_total+equip_peso
                                precio_total=precio_total+40000
                        except:
                            print("Ingrese un peso valido")
                    print(f"El peso de su equipaje es {peso_total} \n Valor: {precio_total}")
                    pesoagregado=True #Ya agregado el equipaje la variable booleana se cambia a True
                    pago=True
                    break
            
            #Restar equipaje
            
            if op2==2:
                if pesoagregado==False: #se comprueba que tenga agregado equipaje
                    print("No haz agregado equipaje")
                else:
                     while True:
                        try:
                            equip_desabastecer=int(input("Ingresa la cantidad de equipo que va a restar: "))
                            if equip_desabastecer<0 or equip_desabastecer>equip_abast: #se valida que la cantidad de equipaje que quiere restar no sea mayor a la que ingreso o menor  a 0
                                print("Ingrese una cantidad valida no puedes quitar mas equipaje del que ingresaste")
                            else:
                                break
                        except:
                            print("Ingresa una cantidad valida (ejemplo: 3)")
                            break
                     
                     for i in range(equip_desabastecer):
                        try:
                            equip_peso=int(input("Ingrese el peso del equipaje (min: 10kg): "))
                            if equip_peso>peso_total:
                                print("no puedes quitar mas peso del que agregaste")
                            elif equip_peso<10:
                                print("Ingrese un peso valido")
                            elif 20>equip_peso>=10:
                                peso_total=peso_total-equip_peso
                                precio_total=precio_total-10000
                            elif 20<=equip_peso<30:
                                peso_total=peso_total-equip_peso
                                precio_total=precio_total-20000
                            elif equip_peso>=30:
                                peso_total=peso_total-equip_peso
                                precio_total=precio_total-40000
                        except:
                            print("Ingrese un peso valido")
                     if peso_total==0:
                            precio_total=0
                            pesoagregado=False
                            pago=False
                     print(f"El peso de su equipaje es {peso_total} \n Valor: {precio_total}$")
                     if op2==3:
                            print("Volviendo al menu principal")
                     
                
    
    if op==2:
            if pesoagregado==False:
                print("No haz agregado equipaje")
            else:
                if 0<edad<=15:                                  #Se valida la edad y se aplican descuentos correspondientes
                    print(f"no obtienes descuento el total a pagar es: {precio_total}$")
                elif 17<=edad<=59:
                    print(f"Precio total: {precio_total}$")
                    precio_total=precio_total*0.85
                    print(f"obtienes descuento del 15 porciento el total a pagar es: {precio_total}$")
                elif edad>=60:
                    print(f"Precio total: {precio_total}$")
                    precio_total=precio_total*0.8
                    print(f"obtienes descuento del 20 porciento el total a pagar es: {precio_total}$")
                while True:
                    try:
                        pagar=int(input("Ingrese la cantidad que va a pagar: "))
                        if pagar<0 or pagar>precio_total :
                            print("Ingrese una cantidad valida (No puedes pagar mas de la cuenta o menos de 0)")
                        elif precio_total-pagar>0:
                            precio_total=precio_total-pagar
                            print(f"Tienes una deuda de {precio_total}")
                        elif precio_total-pagar==0:
                            precio_total=precio_total-pagar
                            pago=False
                            print("Pago realizado con exito")
                            break
                    except:
                        print("Haz ingresado un caracter invalido")
    if op==3:
        if pago==False:
            print("Saliendo del programa")
        else:
            print("Tienes pago pediente!")
            op=0
            continue




