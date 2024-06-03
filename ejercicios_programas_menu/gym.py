print("Gimnasio")

op=0
total_edad=0
hombre=0
mujer=0
total_personas=0
promedio_edad=0
imc_total=0
sobrepeso_hombres=0
bajopeso_mujeres=0
while op!=2:
    print("Menu \n 1.-Calcular IMC \n 2.-Estadisticas")
    try:
        op=int(input("Seleccione una opcion: "))
    except:
        print("Opcion no valida, vuelva a intentarlo")
    from typing import Match
    match op:
        case 1:
            while True:
               try:
                edad=int(input("Ingrese su edad: "))
                if edad>=1:
                   break
                else:
                   print("Ingrese una edad valida")
                   continue
               except:
                    print("Haz ingresado un caracter invalido, vuelva a intentarlo")
                    continue
                
                    
            while True:
                try:
                    estatura=float(input("Ingrese su estatura en metros: "))
                    if estatura>=1:
                        break
                    else:
                        print("ingrese una estatura valida")
                        continue
                except:
                    print("Haz ingresado un caracter invalido")
                    continue
                
            while True:
                try:
                    peso=float(input("Ingrese su peso en kg: "))
                    if peso>=1:
                        break
                    else:
                        print("ingrese un peso valido")
                        continue
                except:
                    print("Caracter invalido vuelvalo a intentar")
                    continue

           
            while True:
                try:
                    sexo=(input("Ingrese su sexo (Masculino/Femenino): ")).lower()
                    if sexo!="masculino" and sexo!="femenino":
                        print("ingrese un sexo valido")
                        continue
                    else:
                        break
                except:
                    print("Dato ingresado no valido vuelva a intentarlo")
                    continue

            if sexo=="masculino":
                imc=peso/ (estatura**2)
                total_edad=total_edad+edad
                hombre=hombre+1
            elif sexo=="femenino": 
                imc=peso/ (estatura**2)
                total_edad=total_edad+edad
                mujer=mujer+1
            peso=round(peso)
            print(f" Edad: {edad} \n Estatura: {estatura} \n Peso: {peso} \n Sexo: {sexo}")
           
           
            if imc<16.00:
                print(f" Infrapeso: Delgadez severa")
                bajopeso_mujeres=bajopeso_mujeres+1
            elif 16.00<=imc<=16.99:
                print(f" Infrapeso: Delgadez moderada")
                bajopeso_mujeres=bajopeso_mujeres+1
            elif 17.00<=imc<=18.49:
                print(f" Infrapeso: Delgadez aceptable")
                bajopeso_mujeres=bajopeso_mujeres+1
            elif 18.50<=imc<=24.99:
                print(f" Peso normal")
            elif 25.00<=imc<=29.99:
                print(f" Sobrepeso")
                sobrepeso_hombres=sobrepeso_hombres+1
            elif 30.00<=imc<=34.99:
                print(f" Obeso: tipo I")
            elif 35.00<=imc<=40.00:
                print(f" Obeso: tipo II")
            elif imc>40.00:
                print(f" Obeso: tipo III")
            imc=round(imc, 1)
            
            print(f" IMC: {imc}")
            total_personas=hombre+mujer
            imc_total=imc_total+imc
            imc_promedio=imc_total/total_personas
            imc_promedio=round(imc_promedio, 1)
        case 2:
            promedio_edad=(total_edad)/total_personas
            print(f"Estadisticas \n Hombres evaluados: {hombre} \n Mujeres evaluadas: {mujer} \n Promedio edad mujeres y hombres: {promedio_edad} \n IMC promedio: {imc_promedio} \n hombre con sobrepeso: {sobrepeso_hombres} \n mujeres bajo el peso normal: {bajopeso_mujeres}")
            
          
           
            
        
   
            
            

                
            
                

                
               
   
           

            