import csv
import funciones as fn
productos = ["leche", "pan", "arroz", "frijoles", "aceite", "huevos", "pollo", "carne",
             "pasta", "queso"]
ventas=[]
op=0

while op!=5:
    try:
        print("Menu \n 1.-Asignar ventas aleatorias \n 2.-Clasificar ventas \n 3.-Ver estadisticas \n 4.-Reporte de ventas \n 5.-Salir del programa")
        op=int(input("Seleccione una opcion: "))
    except ValueError:
        print("Haz ingresado un caracter invalido")
        continue
    if op == 1:
        fn.asignar_ventas_aleatorias(productos, ventas)
    elif op == 2:
        fn.clasificar_venta(ventas)
    elif op == 3:
        fn.ver_estadistica(ventas, productos)
    elif op == 4:
        fn.reporte_ventas(ventas)
    elif op == 5:
        print("Saliendo del programa")
    else:
        print("Seleccione una opcion valida")