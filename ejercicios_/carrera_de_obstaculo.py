print("Comienza la Carrera")

respuesta = str(input("The haz encontrado una valla? si/no. "))

if respuesta == "si":
    print ("Salta la valla!")
elif respuesta == "no":
    print ("Pues sigue corriendo!")

respuesta = str(input("Te haz encontrado un tunel? si/no. "))

if respuesta == "si":
    print ("Pues atraviesa ese tunel!")
elif respuesta == "no":
    print ("Pues sigue corriendo!")

while True:
    respuesta1= str(input("Te haz encontrado una laguna? si/no. "))
    if respuesta1 == "si":
        print("pues a nadar, oh no se ha cansado y se ve forzado a volver.")
        break
    elif respuesta1 == "no":
        print("Pues vamos sigue corriendo, Y LO LOGRASTE FELICIDADES HAZ GANADO LA CARRERA")

print("Fin de la carrera")

    
