plan_tv={
    "Plata": {"precio": 15000, "canales":"45 canales"},
    "Oro": {"precio": 25000, "canales":"65 canales + 10 HD"},
    "Platino":{"precio": 40000, "canales":"90 canales + 30 HD"}
}
tv_on_demand={
    "netflix":{"activo":False, "precio": 6500},
    "star max":{"activo":False, "precio": 9500},
    "disney +":{"activo":False, "precio": 10500 }
}
op=0
total=0
precio_ondemand=0
while True:
    print("=========")
    print("Movi chan")
    for i, (plan,contenido)in enumerate(plan_tv.items()):
        print(f"{i+1}.-{plan} {contenido["canales"]}: {contenido["precio"]}$ ")
    try:
        op=int(input("Seleccione una opcion: "))
        if op>3 or op<1:
            print("seleccione una opcion valida")
            continue
    except ValueError:
        print("Haz ingresado un caracter invalido")
        continue
    plan_escogido=list(plan_tv.keys())[op-1]
    total+=plan_tv[plan_escogido]["precio"]
    print(f"Haz Seleccionado el plan {plan_escogido}")
    break
while op!=4:
    print("=========")
    print("Tv on demand")
    for i, (servicio,contenido) in enumerate(tv_on_demand.items()):
        print(f"{i+1}.-{servicio}: {contenido["precio"]}$")
    print("4.-No deseo tv on demand")
    try:
        op=int(input("Seleccione una opcion: "))
        if op<1 or op>4:
            print("seleccione una opcion valida")
            continue
    except:
        print("Haz ingresado una caracter invalido")
        continue
    if op==4:
        print("No contratas Tv on demand")
    else:
        tvondeman_name=list(tv_on_demand.keys())[op-1]
        
        if tv_on_demand[tvondeman_name]["activo"]==False:
            precio_ondemand+=tv_on_demand[tvondeman_name]["precio"]
            tv_on_demand[tvondeman_name]["activo"]=True
            print(f"Contratas {tvondeman_name} por {tv_on_demand[tvondeman_name]["precio"]}$ \nTotal a pagar {total}$")
        else:
            print("Ya haz contratado ese servicio")
    while True:
        rsp=input("Deseas contratar otro servicio on demand (si/no): ").lower()
        if rsp!="no" and rsp!="si":
            print("Ingrese una opcion valida")
        elif rsp=="si":
            break
        elif rsp=="no":
            op=4
            break
print("=========")
print("Decodificadores")
while True:
    try:
        deco=int(input("Deseas agregar decodificadores adicionales a 3000$ cada uno (si no deseas agregar pon: 0,  max=6): "))
        if deco<0 or deco>6:
            print("Ingrese una cantidad valida")
    except ValueError:
        print("Haz ingresado un caracter invalido")
        continue
    if deco==0:
        print("no llevas decodificadore extras")
        break
    else:
        total+=3000*deco
        print(f"Llevas {deco} decodificador(es) extras por: {3000*deco}$ ")
        break
print("===========")
print("Ya falta poco! solo te falta escoger tu forma de pago")
while True:
    pat=input("Deseas pagar con PAT(pago automatico con tarjeta) (si/no): ").lower()
    if pat!="si" and pat!="no":
        print("Ingrese una respuesta valida")
    elif pat=="si":
        print("================")
        precio_ondemand*0.85
        total+=precio_ondemand
        print("Haz recibido un descuento del 15% por pagar con pat en tu servicio on demand (si es que contrataste alguno)")
        print(f"total a pagar: {total}$")
        break
    elif pat =="no":
        print("================")
        print(f"Total a pagar: {total}$")
        break


    
   