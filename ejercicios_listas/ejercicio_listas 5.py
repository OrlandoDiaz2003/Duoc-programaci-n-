productos=["leche", "huevos", "carne", "pan", "mantequilla"]
Precio_productos=[1000, 4900, 7000, 1500, 1000]
Productos_llevar=[]
total=0
op=0
from typing import Match
while op!=4:
    print("Menu de compras \n 1.-Agregar productos \n 2.-Ver canasta \n 3.-Ver total \n 4.-Salir")
    try:
        op=int(input("Seleccione una opcion: "))
        if op>4 or op<1:
            print("seleccione una opcion valida")
    except:
        print("Haz ingresado un caracter invalido")
        continue
    match op:
        case 1:
            print("=================")
            print("Productos")
            for elemento,precios in zip(productos, Precio_productos):
                print(f"{elemento}: {precios}$")
            print("=================")
            while True:
                escoger_producto=input("Ingrese el producto que desea llevar(leche,carne, etc): ").lower()
                if escoger_producto not in productos:
                    print("Seleccione una opcion valida")
                    continue
                else:
                    if escoger_producto not in Productos_llevar:
                        Productos_llevar.append(escoger_producto)
                
                    posicion_producto=productos.index(escoger_producto)
                    total=total+Precio_productos[posicion_producto]
                    print(f"Llevas {escoger_producto} por {Precio_productos[posicion_producto]}$")
                    print(f"Total: {total}$")
                    break
        case 2:
            print("===============")
            print("Canasta")
            if len(Productos_llevar)==0:
                print("No tienes productos agregados")
            else:
                for elemento in Productos_llevar:
                    print(elemento)
                print(f"Por {total}$")
        case 3:
            print("El total a pagar por los productos es")
            print(f"{total}$")
              
      


                    
                
                

