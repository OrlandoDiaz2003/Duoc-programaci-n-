print("Verduleria")
op=0
total=0
while op!=3:
    print("Menu \n 1.-Comprar \n 2.-Pagar \n 3.-Salir")
    while True:
        try:
            op=int(input("seleccione una opcion: "))
            if op>3:
                print("seleccione una opcion valida")
            else:
                break
        except:
            print("Haz ingresado un caracter invalido vuelva a intentarlo")
            continue
    from typing import Match
    match op:
        case 1:
            print(" Papas 3 kilos 2000$ \n naranjas 1 kilo a 1000$ \n Limon a 1000$")
            while True:
                comprar=(input("Escriba lo que quiere llevar (papas/naranjas/limon): ")).lower()
                if comprar!="papas" and comprar!="naranjas" and comprar!="limon":
                    print("Escriba una opcion valida")
                else:
                    break
            
            if comprar=="papas":
                total=total+2000
                print(f"Haz comprado papas total: {total}")
            
            elif comprar=="naranjas":
                total=total+1000
                print(f"haz comprado naranjas total: {total}")
            
            elif comprar=="limon":
                total=total+1000
                print(f"haz comprado limon total: {total}")
                
        case 2:
            while total!=0:
                try:
                    pagar=int(input("Ingrese cuanto va a pagar (debes pagar el total de la compra): "))
                    if pagar>total:
                        print("no puedes pagar mas de lo que compraste")
                    else:
                        total=total-pagar
                        print(f"Pagando.... \n haz pagado {pagar} \n tu deuda es de {total}")
                
                except:
                    print("haz ingresado un caracter invalido")
                    continue
            print("pago efectuado")
        
        case 3:
            if total!=0:
                print(f"Ey! aun no terminas de pagar deuda: {total}$")
                op=0
            else:
                print("Adios, disfruta la compra")
        