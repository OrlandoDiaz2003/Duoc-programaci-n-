import csv
def agregar_atraccion(atracciones):
    nombre_atraccion=input("Ingrese el nombre de la atraccion: ").lower()
    while True:
        try:
            print("Tipos de atracciones \n 1.-Montaña Rusa \n 2.-Carrusel \n3.-Casa Embrujada")
            rsp=int(input("Seleccione el tipo de atraccion: "))
            if rsp==1:
                clasificacion="montaña rusa"
                break
            elif rsp==2:
                clasificacion="carrusel"
                break
            elif rsp==3:
                clasificacion="casa embrujada"
                break
            else:
                print("Seleccione una opcion valida")
                continue
        except ValueError:
            print("Haz ingresado un caracter invalido")    
            continue
    atraccion={
        "nombre":nombre_atraccion,
        "clasificacion":clasificacion,
        "estado":"operativa"
    }
    atracciones.append(atraccion)


def modificiar_estado(atracciones):
    print("Atracciones")
    estado=0
    for i,datos in enumerate(atracciones, 1):
        print(f"{i}.-Atraccion: {datos['nombre']} Estado:{datos['estado']}")
    while estado!=1 and estado!=2:
        rsp=input("Ingrese el nombre de la atraccion que deseas modificar: ")
        for datos in atracciones:
            if datos['nombre']==rsp:
                print(f"Haz seleccionado {datos['nombre']} \n Estado: {datos['estado']}")
                estado=int(input("En que estado deseas dejar la atraccion \n 1.-Operativa \n 2.-En Mantenimiento \n selecciona una opcion: "))
                if estado==1:
                    datos['estado']="operativa"
                    break
                elif estado==2:
                    datos['estado']="en mantenimiento"
                    break
                else:
                    print("Ingrese una respuesta valida")
                    continue

        else:
            print("xd")
    print("La atraccion ha sido actualizada")

def eliminar_atraccion(atracciones):
    print("Atracciones")
    for i,datos in enumerate(atracciones,1):
        print(f"{i}.-{datos['nombre']}")
    while True:
        try:
            rsp=int(input("Seleccione la atraccion que desea eliminar: "))
            del atracciones[rsp]
        except:
            print("Error vuelva a intentarlo")



    