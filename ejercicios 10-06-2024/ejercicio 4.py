tareas=[]
def añadir_tarea():
    añadir=(input("Ingrese una nueva tarea: "))
    tareas.append(añadir)
    print("Se ha añadido nueva Tarea")

def mostrar_tareas():
    print("Tareas")
    for i,tarea in enumerate(tareas):
        print(f"{i+1}.-{tarea}")
op=0
while op!=3:
    try:
        print("Menu \n1.- Añadir tarea \n2.- Mostrar tareas \n3.- Salir")
        op=int(input("Seleccione una opcion: "))
        if op>3 or op<0:
            print("Ingrese una opcion valida")
            continue
        else:
            if op==1:
                añadir_tarea()
            elif op==2:
                mostrar_tareas()
    except ValueError:
        print("haz ingresado un caracter invalido")
        
    
    
