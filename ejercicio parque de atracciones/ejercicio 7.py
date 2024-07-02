import csv
import func_atracciones as fn
atracciones =[]
atracciones_eliminadas=[]
op=0
while op!=5:
    try:
        print("======================")
        print("Menu \n 1.-Agregar Atraccion \n 2.-Modificar Estado de la Atraccion \n 3.-Eliminar Atraccion \n 4.-Ver Atracciones Eliminadas \n 5.-Salir")
        print("======================")
        op=int(input("Seleccione una opcion: "))
    except ValueError:
        print("haz ingresado un caracter invalido")
    if op==1:
        fn.agregar_atraccion(atracciones)
    elif op==2:
        if len(atracciones)==0:
            print("No haz agregado ninguna atraccion")
        else:
            fn.modificiar_estado(atracciones)
    elif op==3:
        fn.eliminar_atraccion(atracciones, atracciones_eliminadas)
    elif op==4:
        fn.ver_atracciones_eliminadas(atracciones_eliminadas)
    elif op==5:
        print("Saliendo del programa")
    else:
        print("Ingrese una opcion valida")