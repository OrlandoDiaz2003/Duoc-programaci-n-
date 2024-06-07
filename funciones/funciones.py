#def funcion_sencilla():
#    print("Hola, soy una funcion xd")
#funcion_sencilla()

#def suma():
 #   num1 = 2
  #  num2 = 3
   # return(num1 + num2)

#print(suma())

#def suma_ (a,b):
#    sumar = a+b
#    print(f"La suma de los argumentos es: {sumar}")
#num1 = int(input("Ingrese el primer numero: "))
#num2 = int(input("Ingrese el segundo el numero: "))

#suma_(num1, num2)

#def suma_return(a,b):
#    sumar = a + b
#    return(sumar)
#num1 = int(input("Ingrese primer numero: "))
#num2 = int(input("Ingrese el segundo numero: "))

#print(suma_return(num1,num2))

def resta(a, b):
    return a - b
resta(30, 10)
print(resta(30,10))

def resta(a,b):
    return a - b
resta(b=3, a=10)
print(resta(b=3, a=10))

def funcion():
    return "Bienvenidos a python"
frase=funcion()
print(frase)

def calculo(a=None, b=None):
    if a == None or b == None:
        print("Error, falta parametros a la funcion")
        return
    return a - b
print(resta(1,2))

def calcula(precio, descuento):
    return precio - (precio * descuento / 100)
datos = (10000, 10)
print("El monto final a pagar es: ", calculo(*datos))

def saludo(nombre, mensaje = "Python"):
    print(mensaje, nombre)
saludo(mensaje= "Buen dia", nombre="Pedro")