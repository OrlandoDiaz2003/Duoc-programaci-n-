def agregar_jugador(jugadores):
    nombre=input("Ingrese el nombre del jugador: ")
    equipo=input("Ingrese el nombre del equipo: ")
    goles=int(input("Ingrese la cantidad de goles: "))
    jugador={
        "nombre":nombre,
        "equipo": equipo,
        "goles": goles
    }
    jugadores.append(jugador)
    print(jugadores)

def actualizar_goles(jugadores):
    for i, datos in enumerate(jugadores, 1):
        print(f"{i}.-{datos['nombre']}: goles: {datos['goles']}" )

    while True:
        try:
            rsp=int(input("Seleccione al jugador que desea actualizar sus goles: "))
            rsp-=1
            if rsp<0:
                print("Ingrese un respuesta valida")
                continue
            else:
                print(f"Haz seleccionado a {jugadores[rsp]['nombre']} con goles: {jugadores[rsp]['goles']}")
                break
        except ValueError:
            print("Haz ingresado un caracter invalido")
    while True:
        try:
            gol=int(input("Ingrese la cantidad de goles que ha anotado: "))
            if gol<0:
                print("No puedes restar goles")
            else:
                jugadores[rsp]["goles"]+=gol
                print(f"{jugadores[rsp]['nombre']} \n goles actualizados: {jugadores[rsp]['goles']}")
                break
        except ValueError:
            print("Haz ingresado un caracter invalido")

def eliminar_jugador(jugadores):
    for i, datos in enumerate(jugadores, 1):
        print(f"{i}.-{datos['nombre']}" )

    while True:
        try:
            rsp=int(input("Seleccione al jugador que desea eliminar: "))
            rsp-=1
            if rsp<0:
                print("Ingrese un respuesta valida")
                continue
            else:
                print(f"Eliminando a {jugadores[rsp]['nombre']}")
                jugadores.pop(jugadores[rsp])
                break
        except ValueError:
            print("Haz ingresado un caracter invalido")

def mostrar_top_jugadores(jugadores):
    mejores_jugadores=sorted(jugadores, key=lambda x: x["goles"], reverse=True)
    for i,jugador in enumerate(mejores_jugadores, 1):
        print(f"{i}.-{jugador['nombre']}: goles: {jugadores['goles']}")