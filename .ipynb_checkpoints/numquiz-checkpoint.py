import random

Valor_maximo_num = input("Ingresa el rango maximo de nuestro programa\n")

if Valor_maximo_num.isdigit():
    Valor_maximo_num = int(Valor_maximo_num)
    
    if Valor_maximo_num <=0:
        print ("Por favor, ingresa un numero mayor a 0")
        quit()

else:
    print ("Por favor, ingresar un valor numerico")
    quit()


Numero_random = random.randint(0,Valor_maximo_num)
Intentos = 0

while True:
    Intentos += 1 
    Numero_adivinado = input("Intenta Adivinar el numero, ingresa el numero que crees que sea\n")
    if Numero_adivinado.isdigit():
        Numero_adivinado = int(Numero_adivinado)
    
    else:
        print("Por favor trata de que tu adivinanza sea un numero")
        continue

    if Numero_adivinado == Numero_random:
        print ("Muy bien, Adivinaste el numero!!")
        break
    elif Numero_adivinado > Numero_random:
        print ("El numero Ingresado esta por encima del numero generado por el programa")
    else: 
        print ("El numero Ingresado esta por debajo del numero generado por el programa")
        

print ("Las veces que intentaste hasta que adivinaste fueron:", Intentos)
























