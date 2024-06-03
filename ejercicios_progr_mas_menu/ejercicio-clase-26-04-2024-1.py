print("programa")

op=0
tarjeta=100000
#se inicia el menu con bucle while
while op!=3:
    print("Menu \n 1.-Pago de tarjeta de credito \n 2.-Simulacion de compras \n 3.-Salir")
    try:     #try para vereficar que la opcion que seleccione el usuario es correcta
        op=int(input("Seleccione una opcion: "))
    except:
        print("opcion invalida, vuelva a intentarlo")
    from typing import Match

    match op:
        case 1: #primera opcion pago de tarjeta
            try:
                while True:
                    tarjetapay=int(input("Ingrese el precio del producto: "))
                    if 0<=tarjetapay<100000:
                        tarjeta=tarjeta-tarjetapay
                        print(f"saldo de la tarjeta {tarjeta}")
                        break
                    else:
                        print("el monto no puede ser mayor a la deuda o menor a 0")
            except:
                print("haz ingresado un caracter invalido, vuelva a intentarlo")
                continue
        case 2: #segundo opcion simulacion de compras
            while True:
                try:
                    cantidad_product=int(input("Ingrese la cantidad de producto que desea llevar: "))
                    if cantidad_product>0:
                        break
                except:
                    print("haz ingresado un caracter invalido, vuelva a intentarlo")
                    continue
            
            for i in range(cantidad_product): #ciclo for donde el usuario ingresara el valor de los productos
                try:
                    compra=int(input(f"producto numero {i}: "))
                except:
                    print("haz ingresado un caracter invalido, vuelva a intentarlo")
                    break
                if compra>100000 or compra<0:
                    print("el monto no puede ser mayor a la deuda o menor a 0, vuelva a intentarlo")
                    break  #si el usuario ingresa valores no validos o que no cumplan las condiciones el bucle se para y tendra volver a seleccionar la opcion
                else:
                    tarjeta=compra+tarjeta
            print(f"saldo de tarjeta: {tarjeta}")
        case 3:
            print(f"saliendo del programa \n saldo de la tarjeta: {tarjeta}")
                

               
                
            
            