import csv
def comprar_boleto(boletos):
    nombre=input("Ingrese el nombre de la persona que comprar el boleto: ").lower()
    hora=input("Ingrese la hora en que se compra el boleto: ")
    correo=input("Ingrese el correo del comprador: ").lower()
    while True:
        destinos=["viña del mar","valparaiso","concon","santiago"]
        destino=input("Ingrese el destino del boleto: ").lower()
        if destino not in destinos:
            print("Destino no valido")
            continue
        else:
            break
    boleto_comprador={
        'nombre':nombre,
        'hora':hora,
        'correo':correo,
        'estado':"pendiente",
        'destino':destino
    }
    boletos.append(boleto_comprador)
    print("Boleto agregado")

def confirmar_boleto(boletos):
    buscar_correo=input("Ingrese el correo de comprador: ")
    for datos in boletos:
        if datos['correo']==buscar_correo:
            print(f"Comprador \n Nombre: {datos['nombre'].title()} \n Estado: {datos['estado']}")
            while True:
                rsp=input("Deseas confirmar este boleto(s/n): ")
                if rsp =="s":
                    datos['estado']="confirmado"
                    print("Confirmacion completada")
                    break
                elif rsp=="n":
                    print("No se han hecho cambios en el boleto")
                    break
                else:
                    print("Ingrese una respuesta valida")
                    continue
            break
    else:
        print("Este correo no esta en la lista")

def eliminar_boleto(boletos):
    buscar_correo=input("Ingrese el correo de comprador que sea eliminar boleta: ")
    for datos in boletos:
        if datos['correo']==buscar_correo:
            print(f"Comprador \n Nombre: {datos['nombre'].title()} \n Estado: {datos['estado']}")
            while True:
                rsp=input("Deseas eliminar este boleto(s/n): ")
                if rsp =="s":
                    boletos.remove(datos)
                    print("Eliminacion completada")
                    break
                elif rsp=="n":
                    print("No se han hecho cambios en el boleto")
                    break
                else:
                    print("Ingrese una respuesta valida")
                    continue
            break
    else:
        print("Este correo no esta en la lista")

def exportar_registro(boletos):
    with open ("boletas.csv", "w", newline="") as archivo:
        escritor_csv=csv.writer(archivo) 
        escritor_csv.writerow(["Nombre","Hora","Correo","Estado","Destino"])
        for datos in boletos:
            escritor_csv.writerow([
                datos['nombre'],
                datos['hora'],
                datos['correo'],
                datos['estado'],
                datos['destino']
            ])  
    print("Datos exportado")