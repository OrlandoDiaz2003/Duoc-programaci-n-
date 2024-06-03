admin="admin"
admin_password="iamadmin"
discos_duros=10
memoria_ram=3
placas_madre=10
fuentes_de_poder=0
user=0
user_password=0
shoper_user=0
password_shoper=0
op=0
opshoper=0
total=0
pago=False
compra=False
descuento="DESCUENTODELMES"
while op!=2:
    try:
        print("====================")
        print("Menu \n 1.-Iniciar sesion \n 2.-Salir")
        print("====================")
        op=int(input("Seleccione una opcion: "))
        if op>2 or op<1:
            print("Ingrese una opcion valida")
            continue
    except:
        print("Haz ingresado un caracter invalido")
        continue
    if op==1:
        while True:
            user=(input("Ingrese su usuario: "))
            if user!=shoper_user and user!=admin:
                print("Ingrese un usuario valido")
                continue
            else:
                break
        if user==admin:
            while True:
                user_password=input("ingrese su contraseña de administrador: ")
                if user_password!=admin_password:
                    print("Contraseña incorrecta")
                    continue
                else:
                    break
            print("Bienvenido administrador")
            opadmin=0
            while opadmin!=4:
                try:
                    print("====================")
                    print("Menu Admin \n 1.-Dar de alta usuario \n 2.-Abastecer Local \n 3.-Sacar Reporte \n 4.-Cerrar sesion")
                    print("====================")
                    opadmin=int(input("Seleccione una opcion: "))
                    if opadmin>4 or opadmin<1:
                        print("Ingrese una opcion valida")
                        continue
                except:
                    print("Haz ingresado un caracter invalido")
                    continue
                if opadmin==1:
                    shoper_user=input("Cree un usuario de compras: ")
                    password_shoper=input("Cree su contraseña: ")
                    print("Usuario creado, puede iniciar sesion para comprar")
                elif opadmin==2:
                    while True:
                        try:
                            product_abastecer=int(input("Ingrese cuantos productos deseas abastecer (min=1 , max=4): "))
                            if product_abastecer<1 or product_abastecer>4:
                                print("Ingrese una opcion valida")
                                continue
                            else:
                                break
                        except:
                            print("Haz ingresado un caracter invalido")    
                            continue
                    for i in range(product_abastecer):
                        try:
                            print("Productos \n 1.-Disco Duros \n 2.-Memoria ram \n 3.-Placas madre \n 4.-Fuentes de poder")
                            product_select=int(input("seleccione un producto a abastecer: "))
                            if product_select==1:
                                abastecer=int(input("Ingrese la cantidad a abastecer: "))
                                discos_duros=discos_duros+abastecer
                                print(f"Haz agregado {abastecer} discos duros total: {discos_duros}")
                            elif product_select==2:
                                abastecer=int(input("Ingrese la cantidad a abastecer: "))
                                memoria_ram=memoria_ram+abastecer
                                print(f"Haz agregado {abastecer} memorias ram total: {memoria_ram}")
                            elif product_select==3:
                                abastecer=int(input("Ingrese la cantidad a abastecer: "))
                                placas_madre=placas_madre+abastecer
                                print(f"Haz agregado {abastecer} placas madres total: {placas_madre}")
                            elif product_select==4:
                                abastecer=int(input("Ingrese la cantidad a abastecer: "))
                                fuentes_de_poder=fuentes_de_poder+abastecer
                                print(f"Haz agregado {abastecer} fuentes de poder total: {fuentes_de_poder}")
                        except:
                            print("Haz ingresado una opcion invalida")
                elif opadmin==3:
                    print(f"Reporte \n -Discos duros: {discos_duros} \n -Memoria Ram: {memoria_ram} \n -Placas Madre: {placas_madre} \n -Fuentes De Poder: {fuentes_de_poder}")
        elif user==shoper_user:
            while True:
                user_password=input("ingrese su contraseña de comprador: ")
                if user_password!=password_shoper:
                    print("Contraseña incorrecta")
                    continue
                else:
                    break
            print(f"bienvenido {user}")
            opshoper=0
            while opshoper!=3:
                print("======================================")
                print("Bienvenido a la tienda ComputerFactory \n 1.-Comprar productos \n 2.-Pagar cuenta \n 3.-Cerrar sesion")
                print("======================================")
                
                try:
                    opshoper=int(input("Seleccione una opcion: "))
                    if opshoper<1 or opshoper>3:
                        print("Ingrese una opcion valida")
                        continue
                except:
                    print("Haz ingresado un caracter invalido")
                    continue
                if opshoper==1:
                    compra=True
                    print("Productos \n 1.-Discos duros: 50.000$ \n 2.-Memoria Ram: 35.000$ \n 3.-Placas Madre: 40.000$ \n 4.-Fuentes De Poder: 40.0000$ ")
                    while True:
                        try:
                            compra_producto=int(input("Seleccione algun producto: "))
                            if compra_producto<0 or compra_producto>4:
                                print("Ingrese una opcion valida")
                            else:
                                break
                        except:
                            print("Haz ingresado un caracter invalido")
                            continue
                    if compra_producto==1:
                        while True:
                            try:
                                cantidad_productos=int(input("Cuantos discos duros deseas llevar?: "))
                                if cantidad_productos<1:
                                    print("Ingrese una cantidad valida")
                                    continue
                                if discos_duros==0:
                                    print("No hay suficiente stock")
                                    break
                                if discos_duros-cantidad_productos<0:
                                    print("No hay suficiente stock disminuya la cantidad que va a llevar")
                                    continue
                                else:
                                    discos_duros=discos_duros-cantidad_productos
                                    total=total+(cantidad_productos*50000)
                                    print(f"Haz agregado disco duro: {cantidad_productos} \n Valor total: {total}")
                                    pago=True
                                    break
                            except:
                                print("Haz ingresado un caracter invalido: ")
                                continue
                    elif compra_producto==2:
                        while True:
                            try:
                                cantidad_productos=int(input("Cuanta memoria ram deseas llevar?: "))
                                if cantidad_productos<1:
                                    print("Ingrese una cantidad valida")
                                    continue
                                if memoria_ram==0:
                                    print("No hay suficiente stock")
                                    break
                                if memoria_ram-cantidad_productos<0:
                                    print("No hay suficiente stock disminuya la cantidad que va a llevar")
                                    continue
                                else:
                                    memoria_ram=memoria_ram-cantidad_productos
                                    total=total+(cantidad_productos*35000)
                                    print(f"Haz agregado memoria ram: {cantidad_productos} \n Valor total: {total}")
                                    pago=True
                                    break
                            except:
                                print("Haz ingresado un caracter invalido: ")
                                continue
                    elif compra_producto==3:
                        while True:
                            try:
                                cantidad_productos=int(input("Cuantas placas madre deseas llevar?: "))
                                if cantidad_productos<1:
                                    print("Ingrese una cantidad valida")
                                    continue
                                if placas_madre==0:
                                    print("No hay suficiente stock")
                                    break
                                if placas_madre-cantidad_productos<0:
                                    print("No hay suficiente stock disminuya la cantidad que va a llevar")
                                    continue
                                else:
                                    placas_madre=placas_madre-cantidad_productos
                                    total=total+(cantidad_productos*40000)
                                    print(f"Haz agregado placa madre: {cantidad_productos} \n Valor total: {total}")
                                    pago=True
                                    break
                            except:
                                print("Haz ingresado un caracter invalido: ")
                                continue
                    elif compra_producto==4:
                        while True:
                            try:
                                cantidad_productos=int(input("Cuantas fuentes de poder deseas llevar?: "))
                                if cantidad_productos<1:
                                    print("Ingrese una cantidad valida")
                                    continue
                                if fuentes_de_poder==0:
                                    print("No hay suficiente stock")
                                    break
                                if fuentes_de_poder-cantidad_productos<0:
                                    print("No hay suficiente stock disminuya la cantidad que va a llevar")
                                    continue
                                else:
                                    fuentes_de_poder=fuentes_de_poder-cantidad_productos
                                    total=total+(cantidad_productos*40000)
                                    print(f"Haz agregado fuente de poder: {cantidad_productos} \n Valor total: {total}")
                                    pago=True
                                    break
                            except:
                                print("Haz ingresado un caracter invalido: ")
                                continue
                elif opshoper==2:
                    if compra==False:
                        print("No haz agregado ningun producto")
                    else:
                        while True:
                            codigo=input("Tienes algun codigo de descuento?(si/no)").lower()
                            if codigo!="si" and codigo!="no":
                                print("Ingrese una respuesta valida")
                                continue
                            else:
                                break
                        if codigo=="si":
                            while True:
                                descuento_user=input("Ingrese el codigo: ")
                                if descuento_user==descuento:
                                    print(f"se ha aplicado un descuento del 10 porciento en el total de su compra \n Total: {total} \n Total+descuento: {total*0.9}")
                                    total=total*0.9
                                    paga=False
                                    break
                                else:
                                    print("Ingrese un codigo valido")
                                    continue
                            while True:
                                try:
                                    pagar=int(input("Ingrese cuanto va a pagar: "))
                                    if pagar>total:
                                            print("no puedes pagar mas del total")
                                            continue
                                    elif pagar<total:
                                            total=total-pagar
                                            print(f"tienes una deuda de {total}")
                                            continue
                                    elif total-pagar==0:
                                        total=total-pagar
                                        print("Compra realizada con exito")
                                        pago=False
                                        compra=False
                                        break
                                except:
                                    print("haz ingresado un caracter invalido")
                                    continue
                        elif codigo=="no":
                            while True:
                                try:
                                    pagar=int(input("Ingrese cuanto va a pagar: "))
                                    if pagar>total:
                                            print("no puedes pagar mas del total")
                                            continue
                                    elif pagar<total:
                                            total=total-pagar
                                            print(f"tienes una deuda de {total}")
                                            continue
                                    elif total-pagar==0:
                                        total=total-pagar
                                        print("Compra realizada con exito")
                                        pago=False
                                        compra=False
                                        break
                                except:
                                    print("haz ingresado un caracter invalido")
                                    continue
                elif opshoper==3:
                    if pago==False:
                        print(f"cerrando sesion adios {user}")
                    else:
                        print("tienes una deuda aun")
                        opshoper=0