def comprar_boleto(boletos):
    nombre=input("Ingrese el nombre de la persona que comprar el boleto: ")
    hora=input("Ingrese la hora en que se compra el boleto: ")
    correo=input("Ingrese el correo del comprador: ")
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
        correo=info['correo']
        correos.append(correo)
    while True:
        boleto_buscar=input("Ingrese el correo del boleto que deseas confirmar: ")
        if boleto_buscar in correos:
            indice_boleto=correos.index(boleto_buscar)
            boletos[indice_boleto]['estado']="Confirmado"
            for datos,info in boletos[indice_boleto].items():
                print(f"{datos}: {info}")
            print("Confirmacion completada")
            break
        else:
            print("Este correo no se encuentra en la lista")
            continue
        

            
        #print(posicion_boleto)