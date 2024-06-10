def calculo_edad():
    while True:
        try:
            año_nacimiento=int(input("Ingrese su año de nacimiento: "))
            if año_nacimiento>2024 or año_nacimiento<1900:
                print("Ingrese una edad valida")
                continue
            else:
                edad=+2024-año_nacimiento   
                print(f"Tu edad es de {edad} año(s)")
                break
        except:
            print("Haz ingresado un caracter invalido")
            continue
calculo_edad()