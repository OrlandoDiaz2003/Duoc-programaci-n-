notas=[]
def promedio_notas():
    for i in range(4):
        while True:
            try:
                nota=int(input(f"Ingrese su nota numero {i+1}: "))
                if 0<nota and nota>10:
                    print("Ingrese una calificacion valida(entre 0 y 10)")
                    continue
                else:
                    notas.append(nota)
                    break
            except:
                print("Haz ingresado un caracter invalido")
                continue
    total=0
    for elementos in notas:
        total=total+ elementos
    promedio=total/(i+1)
    print(f"tu promedio de notas es: {promedio}")

promedio_notas()