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

def confirmar_boleto(boletos,correos):
    for info in boletos:
        correo_buscar = input("Ingrese el correo a buscar: ").lower()
        if info['correo']==correo_buscar:
            print(f"Boleto encontrado \n Nombre: {info['nombre'].title()} \n Estado: {info['estado']}")
            while True:
                rsp=input("Deseas confirmar boleto(s/n): ").lower()
                if rsp=="s":
                    info['estado']="confirmado"
                    print("Confirmacion completada")
                    break
                elif rsp=="n":
                    print("No se ha cambiado el estado")
                    break
                else:
                    print("Ingrese respuesta valida")
                    continue
        break

            
        #print(posicion_boleto)