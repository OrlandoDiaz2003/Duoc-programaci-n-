productos = {
    "Discos Duros":{"stock":10, "precio":50000},
    "Memorias Ram":{"stock":3, "precio":35000},
    "Placas Madre":{"stock":10, "precio":40000},
    "Fuentes De Poder":{"stock":0, "precio":4000}
}
usuarios={
    "root":"iamroot",
    "test":"123"
}
op=0
total=0
pago=False
while op!=2:#bucle del primer menu
    try:
        print("=========")
        print("Menu \n 1.-Iniciar sesion \n 2.-Salir")
        print("=========")
        op=int(input("Seleccione una opcion: "))
        if op<1 or op>2:
            print("Seleccione una opcion valida")
    except ValueError:
        print("Haz ingresado un caracter invalido")
    if op==1:
        while True:#Bucle validacion de usuario
            print("=========")
            print("Inicio de sesion")
            user=input("Ingrese su usuario: ")
            if user not in usuarios:
                print("El usuario ingresado no existe")
            else:
                break
        while True:#bucle validacion de contraseña
            password=input("Ingrese su contraseña: ")
            if password!=usuarios[user]:
                print("Contraseña incorrecta")
            else:
                break
        if user=="root":
            op2=0
            while op2!=4:
                try:
                    print("==============")
                    print("Menu Admin \n 1.-Dar de alta usuario \n 2.-Abastecer Local \n 3.-Sacar reporte \n 4.-Cerrar sesion")
                    print("==============")
                    op2=int(input("Seleccione una opcion: "))
                    if op2>4 or op2<1:
                        print("Seleccion una opcion valida")
                except ValueError:
                    print("Haz ingresado un caracter invalido")
                    continue
                if op2==1:#Dar de alta usuario
                    print("==============")
                    print("Creacion de un usuario de compras")
                    new_user=input("Cree el nombre de usuario: ")
                    new_password=input("Cree la contraseña: ")
                    usuarios[new_user]=new_password
                
                elif op2==2: #Abastecer el local
                    print("==============")
                    print("Abastecer")
                    while True:
                        try:
                            can_abast=int(input("Ingrese cuantos productos desea abastecer (min=1, max=4): "))
                            if can_abast>4 or can_abast<1:
                                print("Ingrese una cantidad valida")
                            else:
                                break
                        except ValueError:
                            print("haz ingresado un caracter invalido")
                    for i in range(can_abast):
                        print("==============") 
                        for i in productos:
                            print(i)
                        print("==============")   
                        while True:
                            produc_abast=input("Ingrese el producto que desea abastecer(eje: memorias ram): ").title()
                            if produc_abast not in productos:
                                print("El producto ingresado no existe")
                            else:
                                break
                        
                        while True:           
                            try:                 
                                print(f"{produc_abast} stock disponible: {productos[produc_abast]["stock"]} ")
                                produc_fill=int(input("Ingrese la cantida que deseas agregar: "))
                                if produc_fill<1:
                                    print("Ingrese una cantidad valida")
                                    continue
                                else:
                                    productos[produc_abast]["stock"]+=produc_fill
                                    break#se agrega el stock nuevo
                            except ValueError:
                                print("Ingrese caracteres validos (1,2,3...)")
                                continue
                elif op2==3:#reporte 
                    print("==========")
                    print("Reporte")
                    for i,(elementos,stock) in enumerate(productos.items()):
                        print(f"{i+1}.-{elementos}:{stock["stock"]}")
                    print("==========")
                elif op2==4:#cierre del menu de admin
                    print(f"Cerrando sesion adios {user}")
        else:
            op3=0
            while op3!=3:#bucle menu de compras
                try:
                    print(f"Bienvenido {user}")
                    print("==============")
                    print("Menu de compras \n 1.-Comprar productos \n 2.-Pagar cuenta \n 3.-Cerrar Sesion")
                    print("==============")
                    op3=int(input("seleccion una opcion: "))
                    if op3<1 or op3>3:
                        print("Ingrese una opcion valida")
                except ValueError:
                    print("Haz ingresado un caracter invalido")
                if op3==1:
                    print("==============")
                    print("Productos")
                    for i,(producto,precio) in enumerate(productos.items()):
                        print(f"{i+1}.-{producto}: {precio["precio"]}$")
                    pago=True
                    while True:
                        try:
                            product_selec=int(input("Seleccion algun producto: "))
                            if product_selec>4 or product_selec<1:
                                print("Seleccione un producto valido")
                            else:
                                product_name=list(productos.keys())[product_selec-1]#product_name variable donde se guarda el nombre del producto
                                if productos[product_name]["stock"]==0:
                                    print("no hay stock de este producto")
                                    continue
                                else:
                                    break
                                
                        except ValueError:
                            print("Haz ingresado un caracter invalido")
                            continue
                    
                    print(f"Haz seleccionado {product_name}")
                    while True:
                        product_can=int(input("Ingrese la cantidad que deseas llevar: "))
                        if product_can<1:
                            print("seleccione una cantidad valida")
                        else:
                            if productos[product_name]["stock"]-product_can<0:
                                print("No hay suficiente stock disponible")
                                continue
                            else:
                                print("===============================")
                                print(f"Llevas {product_can} {product_name} por: {productos[product_name]["precio"]*product_can}$")
                                total+=productos[product_name]["precio"]*product_can
                                print(f"Total a pagar: {total}$")
                                productos[product_name]["stock"]-=product_can
                                break
                if op3==2:
                    print("==========")
                    print("Pago de compra")
                    if pago==False:
                        print("No haz agregado ningun producto")
                    else:
                        while True:
                            rsp=input("Tienes algun codigo de descuento?(si/no): ").lower()
                            if rsp!="si" and rsp!="no":
                                print("Ingrese una respuesta valida")
                            else:
                                break
        
                        if rsp=="si":
                            while True:
                                descuento=input("Ingrese su codigo de descuento: ")
                                if descuento=="DESCUENTODELMES":
                                    print("=============================")
                                    print("Felicidades haz obtenido un descuento del 10%")
                                    print(f"Total a pagar: {total}$ \nTotal a pagar -10%: {total*0.9}$")
                                    total=total*0.9
                                    break
                                else:
                                    print("codigo incorrecto")
                                continue
                            while True:
                                try:
                                    pagar=int(input("Ingrese la cantidad a pagar: "))
                                    if pagar<=0:
                                        print("Ingrese cantidad valida")
                                    else:
                                        if total-pagar<0:
                                            print("No puedes pagar demas")
                                        elif total-pagar>0:
                                            print(f"Eso no es todo el pago aun tienes que pagar {total-pagar}$")
                                            total-=pagar
                                        elif total-pagar==0:
                                            print("Pago completado")
                                            total-=pagar
                                            pago=False
                                            break
                                except ValueError:
                                    print("Haz ingresado caracter invalido")
                                    continue
                        elif rsp=="no":
                            while True:
                                try:
                                    pagar=int(input("Ingrese la cantidad a pagar: "))
                                    if total-pagar<0:
                                        print("No puedes pagar demas")
                                    elif total-pagar>0:
                                        print(f"Eso no es todo el pago aun tienes que pagar {total-pagar}$")
                                        total-=pagar
                                    elif total-pagar==0:
                                        print("Pago completado")
                                        total-=pagar
                                        pago=False
                                        break
                                except ValueError:
                                    print("Haz ingresado caracter invalido")
                if op3==3:
                    if pago==True:
                        print("Tienes una deuda pendiente")
                        op3=0
                    else:
                        print("Adios")