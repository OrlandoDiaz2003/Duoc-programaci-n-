def agregar_jugador(jugadores):
    nombre=input("Ingrese el nombre del jugador: ")
    equipo=input("Ingrese el nombre del equipo en el que juega: ")
    while True:
        try:
            goles=int(input("Ingrese la cantidad de goles que ha anotado: "))
            if goles <0:
                print("Ingrese una cantidad valida")
                continue
            else:
                jugador={
                        "equipo":equipo,
                        "goles": goles
                }
                jugadores[nombre]=jugador
                break
        except ValueError:
            print("Haz ingresado un caracter invalido")
            continue

def actualizar_cantidad_goles(jugadores):
    print("Actualizar cantidad de goles")
    for i,(elementos, data) in enumerate(jugadores.items(), 1):
        print(f"{i}.-{elementos}: goles: {data["goles"]}")
    while True:
        try:
            rsp=int(input("seleccione un jugador: "))
            if rsp<1 or rsp>i:
                print("Seleccione una opcion valida")
            else:
                break
        except ValueError:
            print("Haz ingresado un caracter invalido")                
    escoger=list(jugadores.keys())[rsp-1]
    print(f"Haz seleccionado este jugador: {escoger} goles: {jugadores[escoger]["goles"]}")
    while True:
        try:
            gol_act=int(input("Actualize los goles del jugador: "))
            jugadores[escoger]["goles"]+=gol_act
            break
        except ValueError:
            print("Haz ingresado un caracter invalido")
            continue

def eliminar_jugador(jugadores):
    print("eliminar jugador")
    for i,(elementos, data) in enumerate(jugadores.items(), 1):
        print(f"{i}.-{elementos}")
    while True:
        try:
            rsp=int(input("seleccione un jugador: "))
            if rsp<1 or rsp>i:
                print("Seleccione una opcion valida")
                continue
            else:
                break
        except ValueError:
            print("Haz ingresado un caracter invalido")  
            continue              
    escoger=list(jugadores.keys())[rsp-1]
    print(f"eliminando a este jugador: {escoger}")
    del jugadores[escoger]

def top_jugadores(jugadores, can_goles):
    for elementos,a in jugadores.items():
        can_goles.append(a["goles"])   
    print(sorted(can_goles, reverse=True))   
    