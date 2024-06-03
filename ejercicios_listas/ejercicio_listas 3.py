
op=""
nombres=[]
nombre_pequeño=[]
while True:
    agregar_nombres=input("Ingrese un nombre: ")
    nombres.append(agregar_nombres)
    while True:
        op=input("Desea agrega otro nombre? (si/no): ").lower()
        if op!="si" and op!="no":
            print("seleccione una opcion valida")
            continue
        else:
            break
    if op=="si":
        continue
    elif op=="no":
        print("Borrando el nombre mas pequeño")
        nombre_pequeño = min(nombres ,key=len)
        print(f"el nombre ha borrar {nombre_pequeño}")
        nombres.remove(nombre_pequeño)
        break
print(nombres)
    

            
