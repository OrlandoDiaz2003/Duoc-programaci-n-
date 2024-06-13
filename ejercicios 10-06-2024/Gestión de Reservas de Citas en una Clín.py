import csv
citas_medicas={
    "User":{"medico": "doctor", "fecha":"2024-07-24", "hora":"10:30", "motivo":"consulta general"},
    "User2":{"medico": "doctor", "fecha":"2024-07-24", "hora":"10:30", "motivo":"consulta general"}
}

def agregar_cita():
    agregar_paciente=input("Ingrese el nombre del paciente: ").title()
    medico=input("Ingrese el nombre del medico que atendera al paciente: ").title()
    fecha=input("Ingrese la fecha de la cita (ejemplo 2024-05-24): ")
    hora=input("Ingrese la hora de la cita (ejemplo 10:30): ")
    motivo=input("Ingrese el motivo de la cita: ")
    cita={             #se crea un diccionario anidado donde estan los datos de la cita
        "medico":medico,
        "fecha":fecha,
        "hora":hora,
        "motivo":motivo
    }
    citas_medicas[agregar_paciente]=cita #se guarda los datos del paciente en el diccionario de citas_medicas

def eliminar_citas():
    while True:
        buscar=input("Ingrese el nombre del paciente que desea cancelar su cita: ").title()
        if buscar not in citas_medicas:
            print("Esta persona no se encuentra en la lista")
        else:
            print(f"¿Este es el paciente que desea cancelar su cita? \nPaciente= {buscar} \nFecha de cita: {citas_medicas[buscar]['fecha']}")
            rsp=input("[S/N]: ").lower()
            if rsp=="s":
                del citas_medicas[buscar]
                print("Cita cancelada")
                break
            elif rsp=="n":
                print("Volviendo al buscador de pacientes")
                continue
            else:
                print("Respuesta Invalida")
                print("Volviendo al buscador de pacientes")
                continue

def buscar_citas():
    while True:
        buscar=input("Ingrese el nombre del paciente para ver detalles de su cita: ").title()
        if buscar not in citas_medicas:
            print("El paciente ingresado no se encuentra en la lista")
            continue
        else:
             print(f"Paciente: {buscar}")
             for datos, info in citas_medicas[buscar].items():
                print(f"{datos.title()}: {info}")
        break  

def registro_citas_csv():
    with open("registro_citas.csv" , "w", newline="") as datos_citas: #se crea/abre archivo.csv 
        escritor_csv=csv.writer(datos_citas)
        escritor_csv.writerow(["Paciente", "Medico", "Fecha", "Hora", "Motivo"]) #se ingresan las categorias
        for elemento, info, in citas_medicas.items(): #con un clico for se va iterando en los datos de los pacientes 
            escritor_csv.writerow([
                
                    elemento,                    #elemento es el nombre de los pacientes
                    info["medico"],       #info son los datos de los pacientes 
                    info["fecha"], 
                    info["hora"], 
                    info["motivo"]
                
                ])
    print("Guardando datos en archivo csv")

def menu():

    op=0
    while op!=5:
        try:
            print("========================")
            print("Menu citas medicas \n 1.-Agregar cita \n 2.-Eliminar citas \n 3.- Buscar cita \n 4.-Guardar citas en un archivo csv \n 5.-salir")
            op=int(input("Seleccione una opcion: "))
            if op==1:
                agregar_cita()
            elif op==2:
                eliminar_citas()
            elif op==3:
                buscar_citas()
            elif op==4:
                registro_citas_csv()
            elif op==5:
                print("Saliendo del programa")
            else:
                print("Seleccione una opcion valida")
                continue
        except ValueError:
            print("Ingrese un caracter valido")


menu()