import csv          #se importa csv para poder guardar datos en archivo csv
def agregar_atraccion(atracciones):
    print("======================")
    nombre_atraccion=input("Ingrese el nombre de la atraccion: ").lower() #se pregunta por el nombre de la atraccion
    while True:    #se inicia bucle para validar que la clasificacion que se le de a la atraccion sea la correcta
        try:
            print("Tipos de atracciones \n 1.-Montaña Rusa \n 2.-Carrusel \n 3.-Casa Embrujada")
            rsp=int(input("Seleccione el tipo de atraccion: "))
            if rsp==1:
                clasificacion="montaña rusa"    #se crea variable 'clasificacion' con las distintas respuestas dependiendo de la que escoga
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
    atraccion={                            #Se crea un diccionario que contiene las informacion de la atraccion que se ha agregado
        "nombre":nombre_atraccion,
        "clasificacion":clasificacion,
        "estado":"operativa"
    }
    atracciones.append(atraccion)   #con ".append()" se agrega esta nueva atraccion a la lista de atracciones

def modificiar_estado(atracciones):
    print("======================")
    print("Atracciones")
    estado=0                  #se inicializa variable estado para evitar errores
    for i,datos in enumerate(atracciones, 1):              #con clico for se muestran las atracciones que estan en la lista
        print(f"{i}.-Atraccion: {datos['nombre']} Estado:{datos['estado']}")       #se usa la funcion enumerate para que enumere los datos de la lista con la variable i
    print("======================")                                               #  enumerate(atracciones, 1) se el 1 dentro del parantesis es para que la enumaracion empieze desde este digito
    while estado!=1 and estado!=2:  #se inicia ciclo while para modificar una atraccion
        try:
            rsp=input("Ingrese el nombre de la atraccion que deseas modificar: ")
            for datos in atracciones:   #Se inicia clico for para recorrer los datos de la atraccion escogida
                if datos['nombre']==rsp:   #condicion al recorrer la lista se compara el dato del nombre de la atraccion con el que ingrese el usuario, si estos son iguales se entra en este if
                    print(f"Haz seleccionado {datos['nombre']} \n Estado: {datos['estado']}") 
                    estado=int(input("En que estado deseas dejar la atraccion \n 1.-Operativa \n 2.-En Mantenimiento \n selecciona una opcion: "))
                    if estado==1:
                        datos['estado']="operativa"     #se le da escoger al usuario las distintas opciones para modificar el estado de la atraccion
                        break
                    elif estado==2:
                        datos['estado']="en mantenimiento"
                        break
                    else:
                        print("Ingrese una respuesta valida")
                        continue
            else:                       #else en la misma linea del for, si en todos los recorridos del bucle for ninguno de los nombre de las atracciones de la lista es igual
                print("Esta atraccion no existe")                  #al que ingreso el usuario se entre en el else que indica el error
        except ValueError:
            print("Haz ingresado un caracter invalido")
    print("La atraccion ha sido actualizada")

def eliminar_atraccion(atracciones, atracciones_eliminadas):        #se agrega a atracciones_eliminadas para agregar las atracciones que se eliminen
    print("Atracciones")
    for i,datos in enumerate(atracciones,1):          #Se muestran las atracciones que existen enumeradas del 1 en adelante con enumerate
        print(f"{i}.-{datos['nombre']}")
    while True:
        try:
          
            rsp=int(input("Seleccione la atraccion que desea eliminar: "))   #Se le pide al usuario que escoga alguna de las atracciones
            rsp-=1       #una vez escogida a la respuesta se le resta 1 por los indices de las listas comienza desde el 0, por lo que si desea escoger el primer dato tiene que ingresar 0 en vez de 1

            atracciones_eliminadas.append(atracciones[rsp])  #se agrega la atraccion que quiere eliminar a la lista de atracciones eliminadas, usando la respuesta
                                                        #del usuario almacenada en la variable rsp, esta se usa como indice, si el usuario quiere eliminar la primera atraccion
                                                        #de la lista de atracciones, ingresara 1, a este se le restara 1 y quedara en 0 y para poder agregarlo
                                                        #quedando como 'atracciones[rsp]' osea el primer dato de la lista 
            del atracciones[rsp]     #con 'del' se borra la atraccion escogida de la lista
            break
        except:
            print("Error vuelva a intentarlo")
            continue
    print("Atraccion eliminada")


def ver_atracciones_eliminadas(atracciones_eliminadas):
    while True:          #bucle para validar el inicio de sesion
        usuario=input("Ingrese tu nombre de usuario: ")
        if usuario =="Admin":         
            break
        else:
            print("vuelva a intentarlo")
            continue
    while True:
        Contraseña=input("Ingrese su contraseña: ")
        if Contraseña=="Admin123":
            print("contraseña correcta")
        else:
            print("Contraseña incorrecta")
            continue
       
        for i, datos in enumerate(atracciones_eliminadas, 1): #se muestra en pantalla las atracciones eliminadas
            print(f"{i}.-Atraccion \n Nombre:{datos['nombre']} \n Tipo: {datos['clasificacion']} \n Estado: {datos['estado']}")
        
        with open ("Atracciones_supr.csv","w",newline="") as archivo: #se abre/crea el archivo csv 
            escritor=csv.writer(archivo)            #se crea un escritor de csv que escribira en el 'archivo'
            escritor.writerow(["Nombre", "Tipo", "Estado"])   #se agregan las categorias
            for datos in atracciones_eliminadas:  #con bucle for se recorre los datos la lista de atracciones eliminadas
                escritor.writerow([     #con el escritor se ingresan los datos en el archivo csv
                    datos["nombre"],
                    datos["clasificacion"],
                    datos["estado"]
                ])
        break    
                
                
                
        