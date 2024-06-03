import csv
with open('kematian_pete.csv', 'r') as archivo_csv:
    lector_csv=csv.DictReader(archivo_csv)
    for fila in lector_csv:
        nombre=fila['nombre']
        status=fila['status']
        nivel=int(fila['nivel'])
        print(f"nombre: {nombre} \nstatus: {status} \nnivel: {nivel}")
