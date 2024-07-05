import csv
import random
def asignar_ventas_aleatorias(productos, ventas):
    for datos in productos:
        venta_aleatoria=random.randint(1_000, 10_000)
        venta={
            "producto":datos,
            "ventas":venta_aleatoria,
            "clasificacion":" "
        }
        ventas.append(venta)
def clasificar_venta(ventas):
    for datos in ventas:
        if datos['ventas'] < 3000:
            datos['clasificacion']= "Menor a 3000"
        
        elif 3000<= datos['ventas'] <= 7000:
            datos['clasificacion']= "entre 7000 y 3000"
        
        elif datos['ventas'] > 7000:
            datos['clasificacion']= "Mayor a 7000"

def ver_estadistica(ventas, productos):
    venta_alta=max(ventas, key=lambda x: x['ventas'])
    venta_baja=min(ventas, key=lambda x: x['ventas'])
    venta_total=0
    total_productos=len(productos)

    for datos in ventas:
        venta_total += datos['ventas']
    promedio= venta_total / total_productos
    valores_mul=1
    for datos in ventas:
        valores_mul*=datos['ventas']
    media_gemotrica= valores_mul ** (1 / len(productos))
    
    print("=========================")
    print("Venta mas alta")
    for datos,info in venta_alta.items():
        print(f"{datos}: {info}")
    print("=========================")
    print("Venta mas baja")
    for datos,info in venta_baja.items():
        print(f"{datos}: {info}")
    print("=========================")
    print(f"Promedio de ventas: {promedio}")
    print("=========================")
    print(f"Media geometrica: {media_gemotrica:.2f}")

def reporte_ventas(ventas):
    with open("reporte.csv", "w", newline="") as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow(["producto", "Impuesto 10%", "Descuento 5%", "venta neta"])
        for datos in ventas:
            impuesto=datos['ventas']*0.1
            descuento=datos['ventas']*0.05
            neto=datos['ventas']- impuesto - descuento
            escritor.writerow([
                datos['producto'],
                round(impuesto,2),
                round(descuento,2),
                round(neto,2)
            ])

