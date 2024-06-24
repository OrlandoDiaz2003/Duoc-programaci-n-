import csv
import funciones as fn
boletos=[
    {
        'nombre':"orlando",
        'hora':"10:30",
        'correo':"or.diaz@duoc.cl",
        'estado':"pendiente",
        'destino':"viña del mar"
    },
    {
        'nombre':"kema",
        'hora':"10:30",
        'correo':"kema@duoc.cl",
        'estado':"pendiente",
        'destino':"viña del mar"
    }
]
correos=[]
op=0

while op!=5:
    #try:
        print("Menu \n 1.-Comprar boleto \n 2.-Confirmar boleto \n 3.-Eliminar boleto \n 4.-Exportar registro")
        op=int(input("Seleccione una opcion: "))
        if op==1:
            fn.comprar_boleto(boletos)
        elif op==2:
            fn.confirmar_boleto(boletos,correos)
        elif op==3:
            print()
        elif op==4:
            print()
        elif op==5:
            print()
        else:
            print("Ingrese una opcion valida")
    #except ValueError:
        #print("Haz ingresado un caracter invalido")