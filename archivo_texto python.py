import json
with open ('xd.json','r') as archivo:
    datos_leido= json.load(archivo)
    print(datos_leido)
    