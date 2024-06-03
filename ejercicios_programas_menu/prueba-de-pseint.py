print("tienda")
op=0
bebidas=0
postres=0
platos=0
compra=False
propina=0
total=0
while op!=4:
    try:
        print("=========")
        print("Menu \n 1.-Bebidas: 1000$ \n 2.-Postres: 5000$ \n 3.-Platos de entrada: 7000$ \n 4.-Salir")
        print("=========")
        op=int(input("Seleccione una opcion: "))
        if op>4 or op<0:
            print("seleccione una opcion valida")
            continue
    except:
        print("caracter invalido")
        continue
    if op==1:
        while True:
            try:
                can_bebidas=int(input("cuantas bebidas deseas llevar: "))
                compra=True
                if can_bebidas<0:
                    print("ingrese un valor valido")
                else:
                    for i in range (can_bebidas):
                        bebidas=bebidas+1000
                    print(f"Llevas {can_bebidas} bebida(s) por: {bebidas}")
                    break
            except:
                print("Caracter invalido")
    elif op==2:
        while True:
            try:
                can_postres=int(input("cuantas postres deseas llevar: "))
                compra=True
                if can_postres<0:
                    print("ingrese un valor valido")
                else:
                    for i in range (can_postres):
                        postres=postres+5000
                    print(f"Llevas {can_postres} postre(s) por: {postres}")
                    break
            except:
                print("Caracter invalido")
    elif op==3:
        while True:
            try:
                can_platos=int(input("cuantas platos de entradas deseas llevar: "))
                compra=True
                if can_platos<0:
                    print("ingrese un valor valido")
                else:
                    for i in range (can_platos):
                        platos=platos+7000
                    print(f"Llevas {can_platos} plato(s) por: {platos}")
                    break
            except:
                print("Caracter invalido")
    elif op==4:
        if compra==True:
            while True:
                    try:
                        propina=int(input("¿deseas agregar propina? si no deseas agregar propina ingrese 0: "))
                        if propina<0:
                            print("ingrese un valor valido")
                            continue
                        elif propina==0:
                            total=total+bebidas+postres+platos
                            print(f" Gracias por comprar con nosotros \n Total: {total}$ ")
                            break
                        else:
                            total=total+bebidas+postres+platos
                            print(f" Gracias por comprar con nostros \n Total: {total} \n Total con propina: {total+propina}&")
                            break
                    except:
                        print("caracter invalido")
                        continue
        else:
            print("Adios, espero que encuentres lo que buscas la proxima vez")