import csv
import func_atracciones as fn
atracciones =[]
op=0
while op!=5:
    try:
        print("Menu \n 1.-Agregar Atraccion \n 2.-Modificar Estado de la Atraccion \n 3.-Eliminar Atraccion \n 4.-Ver Atracciones Eliminadas \n 5.-Salir")
        op=int(input("Seleccione una opcion: "))
    except ValueError:
        print("haz ingresado un caracter invalido")
    if op==1:
        fn.agregar_atraccion(atracciones)
    elif op==2:
        fn.modificiar_estado(atracciones)
    elif op==3:
        fn.eliminar_atraccion(atracciones)
    elif op==4:
        print()
    elif op==5:
        print()
    else:
        print("Ingrese una opcion valida")