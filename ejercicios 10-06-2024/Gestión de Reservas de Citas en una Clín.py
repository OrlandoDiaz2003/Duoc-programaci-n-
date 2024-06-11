import csv
citas_medicas={
    "User":{"nombre_medico": "doctor", "fecha":"2024-07-24", "hora":"10:30", "motivo":"consulta general"},
    "User2":{"nombre_medico": "doctor", "fecha":"2024-07-24", "hora":"10:30", "motivo":"consulta general"}
}

def agregar_cita():
    agregar_paciente=input("Ingrese el nombre del paciente: ").title()
    medico=input("Ingrese el nombre del medico que atendera al paciente: ").title()
    fecha=input("Ingrese la fecha de la cita (ejemplo 2024-05-24): ")
    hora=input("Ingrese la hora de la cita (ejemplo 10:30): ")
    motivo=input("Ingrese el motivo de la cita: ")
    citas_medicas[agregar_paciente]=[{"nombre_medico":medico, "fecha":fecha, "hora":hora, "motivo":motivo }]

def eliminar_citas():
    while True:
        buscar=input("Ingrese el nombre del paciente que desea cancelar su cita: ").title()
        if buscar not in citas_medicas:
            print("Esta persona no se encuentra en la lista")
        else:
            print(f"¿Este es el paciente que desea cancelar su cita? \nPaciente= {buscar} \nFecha de cita: {citas_medicas[buscar]["fecha"]}")
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
        buscar=input("Ingrese el nombre del paciente para ver detalles de su cita: ")
        if buscar not in citas_medicas:
            print("El paciente ingresado no se encuentra en la lista")
            continue
        else:
            print(f"{buscar} \nDoctor: {citas_medicas[buscar]["nombre_medico"]} \nFecha: {citas_medicas[buscar]["fecha"]} \nHora: {citas_medicas[buscar]["hora"]} \nMotivo: {citas_medicas[buscar]["motivo"]}")
            break

def registro_citas_csv():
    datos=[]
    with open("registro_citas.csv" , "w", newline="") as datos_citas:
        escritor_csv=csv.writer(datos_citas)
        escritor_csv.writerow(["Paciente", "Medico", "Fecha", "Hora", "Motivo"])
        paciente=list(citas_medicas)
        escritor_csv.writerows([
            citas_medicas
        ])
registro_citas_csv()