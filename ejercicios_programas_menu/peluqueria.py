print("Peluqueria")
from typing import Match
total=0
op=0
while op!=4:
    try:
        print("Menu \n 1 Corte de pelo niño/a 5000$ \n 2 corte de pelo Hombre o Mujer 10000$ \n 3 Corte de pelo Adulto Mayor 4000$ \n 4 Salir ")
        op=int(input("escoga una opcion: "))
    except:
        print("Error, ingrese opcion valida")
    match op:
        case 1:
                    try:
                        edad=int(input("ingrese su edad: "))
                        if 0<edad<=15:
                             print("Haciendo corte niño")
                             total=total+5000
                        else:
                             print("por tu edad deberias escoger otro corte")
                             op=0
                    except:
                         print("ingrese una edad valida")
        case 2:
                    try:
                        edad=int(input("ingrese su edad: "))
                        if 16<edad<=59:
                             print("Haciendo corte hombre/mujer")
                             total=total+10000
                        else:
                             print("por tu edad deberias escoger otro corte")
                             op=0
                    except:
                         print("ingrese una edad valida")
        case 3:
                    try:
                        edad=int(input("ingrese su edad: "))
                        if 60<edad:
                             print("Haciendo corte adulto mayor")
                             total=total+4000
                        else:
                             print("por tu edad deberias escoger otro corte")
                             op=0
                    except:
                         print("ingrese una edad valida")
        case 4:
              print(f"El total seria {total}")
              
                   
                 
                 
               
                
               
                  
                










        
