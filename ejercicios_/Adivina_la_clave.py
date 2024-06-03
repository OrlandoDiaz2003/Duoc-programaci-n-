clave=[]
print("Ingrese 5 digitos con numeros de 0 al 9")
for i in range(5):
    
        while True:
            try:
                digito=int(input())
                if 0>digito or digito>9:
                    print("Ingrese un digito valido")
                    continue
                else:
                    clave.append(digito)
                    break
            except:
                print("Haz ingresado un digito invalido")
print("======================")
print("Jugador 2 tendra que intentar adivinar la clave tienes 6 intentos")
clave_intentos=["*"]*5
intentos=6
while intentos>1:
    try:
        print(f"Intentos restantes: {intentos}")
        if clave_intentos==clave:
            break
        intento=int(input("Ingrese un digito: "))
        if intento in clave:
            posicion=clave.index(intento)
            print("Haz descubierto un digito su posicion es")
            clave_intentos[posicion]=intento
            print(clave_intentos)
        else:
            print("Este digito no se encuentra en la clave")
            intentos=intentos-1
    except:
        print("Ingrese un digito valido 1,2,3.....")
        
if clave_intentos==clave:
    print("============")
    print("Ganaste")
    print(f"Felicidades haz encontrado la clave \n {clave}")
else:
    print("============")
    print("Perdiste")
    print(f"No encontraste la clave \n la clave era \n {clave}")