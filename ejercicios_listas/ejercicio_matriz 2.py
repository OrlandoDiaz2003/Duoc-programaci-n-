arreglos=[
    [
        ["amarillo","rojo","naranja"],
        ["verde","blanco","amarillo"],
        ["rojo","verde","blanco"],

    ],
    [
        ["rojo","amarillo","blanco"],
        ["verde","rojo","naranja"],
        ["amarillo","blanco","rojo"],

    ],
    [
        ["amarillo","blanco","verde"],
        ["blanco","rojo","naranja"],
        ["verde","rojo","blanco"]
    ]  
]
amarillo=0
rojo=0
naranja=0
verde=0
blanco=0

for dimension in arreglos:
    for fila in dimension:
        for elemento  in fila:
            if elemento=="amarillo":
                amarillo+=1
            elif elemento=="rojo":
                rojo+=1
            elif elemento=="naranja":
                naranja+=1
            elif elemento == "verde":
                verde+=1
            elif elemento== "blanco":
                blanco+=1
print(f" numero de elementos amarillos: {amarillo} \n numero de elementos rojos: {rojo} \n numero de elementos naranja: {naranja} \n numero de elementos verde: {verde} \n numero de elementos blanco: {blanco}")
            
            
            
     