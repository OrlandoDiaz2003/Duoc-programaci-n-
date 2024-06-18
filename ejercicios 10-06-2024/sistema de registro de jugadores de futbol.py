import func_futbol as fn_player 
op=0

jugadores= [
    {
        "nombre":"felipe",
        "equipo": "kali linux",
        "goles": 3
    },
    {
        "nombre":"ronaldiño",
        "equipo": "Ubuntu",
        "goles": 2
    } 
]

while op!=5:
    try:
        print("Menu \n 1.-Agregar jugador \n 2.-Actualizar cantidad de goles \n 3.-Eliminar Jugador \n 4.-Mostrar Top de Jugadores \n 5.-Salir")
        op=int(input("Seleccione una opcion: "))
        if op==1:
           fn_player.agregar_jugador(jugadores)
        elif op == 2:
            fn_player.actualizar_goles(jugadores)
        elif op == 3:
            fn_player.eliminar_jugador(jugadores)
        elif op == 4:
            fn_player.mostrar_top_jugadores(jugadores)
        elif op == 5:
            print()
    except ValueError:
        print("Haz ingresado un caracter invalido")