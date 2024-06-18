import funciones as func_player 
op=0
jugadores={
    "scompry":{"equipo": "geis", "goles":0},
    "kematian":{"equipo": "geis", "goles":2}
}
can_goles=[]

while op!=5:
    try:
        print("Sistema de registro \n 1.-Agregar jugador \n 2.-Actualizar cantidad de goles \n 3.-Eliminar Jugador \n 4.-Mostrar top de jugadores \n 5.-Salir")
        op=int(input("Seleccione una opcion: "))
        if op==1:
            func_player.agregar_jugador(jugadores)
            print(jugadores)
        elif op==2:
            func_player.actualizar_cantidad_goles(jugadores)
        elif op==3:
            func_player.eliminar_jugador(jugadores)
        elif op==4:
            func_player.top_jugadores(jugadores, can_goles)
        elif op==5:
            print()
        else:
            print("Seleccione una opcion valida")
    except ValueError:
        print("Haz ingresado un caracter invalido")
