import numpy as np; import random

def ejercicio1():
    t = 0; p = 0; contador = 0; contador2 = 0 # Variables importantes

    while True:
        try:
            num = int(input("Números de correos: "))
            if num > 0:
                break
        except ValueError:
            pass

    correos = []
    for x in range(num):
        correo = input(f"Ingrese el {x+1} correo: ")
        while True:
            if "@" in correo and "." in correo:
                m = correo.split(".")
                correo = m[-1]
                correos.append(correo)
                break
            else:
                correo = input(f"Ingrese el {x+1} correo: ")

    correos.sort() # Variables importantes

    for x in correos:
        if x == correos[t]:
            contador += 1
            k = x
        else:
            contador2 += 1
            if contador <= contador2:
                contador = contador2
                contador2 = 0
                t = p
            elif x == correos[p-1]:
                pass
            else:
                contador2 = 1
        p += 1
    print(f"{k} - {contador}")
# ejercicio1() # LLAMAR ASÍ AL EJERCICIO.

def ejercicio2():
    num = input("Ingrese el número romano: ")
    romano = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000} # Biblioteca de números romanos
    anterior = 0; guardar = 0; suma = 1; contador = 0; contador2 = 0; a = "Número romano mal ingresado"; b = "Número romano bien ingresado"
    for x in num:
        contador2 += 1
        if x not in romano:
            return a
        
        hola = romano[x];

        match x:
            case "I": # Primer caso
                if x == guardar and suma == 3: # Numeros que se repiten 3 veces
                    return a
                if contador == (len(num)-1):
                    return b
                elif num[contador2] != "I" and num[contador2] != "X":
                    return a
                else:
                    if hola > anterior:
                        guardar = x
                        anterior = hola
                        suma = 1
                    else:
                        suma += 1

            case "X": # Segundo caso
                if x == guardar and suma == 3: # Numeros que se repiten 3 veces
                    return a
                if contador == (len(num)-1):
                    return b
                elif num[contador2] != "L" and num[contador2] != "C" and num[contador2] != "I" and num[contador2] != "X" and [(contador2-2)] == "I":
                    return a
                else:
                    if hola > anterior:
                        guardar = x
                        anterior = hola
                        suma = 1
                    else:
                        suma += 1

            case "C": # Tercer caso
                if x == guardar and suma == 3: # Numeros que se repiten 3 veces
                    return a
                if contador == (len(num)-1):
                    return b
                elif num[contador2] != "D" and num[contador2] != "M" and num[contador2] != "C" and num[contador2] == "I":
                    return a
                else:
                    if hola > anterior:
                        guardar = x
                        anterior = hola
                        suma = 1
                    else:
                        suma += 1
            case "D": # Cuarto caso
                if x == guardar and suma == 1: # Numeros que se repiten 1 veces
                    return a
                if contador == (len(num)-1):
                    return b
                if num[contador2] == "M":
                    return a
                else:
                    if hola > anterior:
                        guardar = x
                        anterior = hola
                        suma = 1
                    else:
                        suma += 1
            case "V": # Quinto caso
                if x == guardar and suma == 1: # Numeros que se repiten 1 veces
                    return a
                if contador == (len(num)-1):
                    return b
                if num[contador2] == "C":
                    return a
                else:
                    if hola > anterior:
                        guardar = x
                        anterior = hola
                        suma = 1
                    else:
                        suma += 1
            case "L": # Sexto caso
                if x == guardar and suma == 1: # Numeros que se repiten 1 veces
                    return a
                if contador == (len(num)-1):
                    return b
                if num[contador2] == "C":
                    return a
                else:
                    if hola > anterior:
                        guardar = x
                        anterior = hola
                        suma = 1
                    else:
                        suma += 1
            case "M":
                if x == guardar and suma == 3: # Numeros que se repiten 3 veces
                    return a
                if contador == (len(num)-1):
                    return b
                else:
                    if hola > anterior:
                        guardar = x
                        anterior = hola
                        suma = 1
                    else:
                        suma += 1
        contador += 1
    return b
# print(ejercicio2()) # LLAMAR ASÍ EL EJERCICIO.

def ejercicio3():
    while True:
        try:
            columnas = int(input("Ingrese las dimensiones: "))
            if columnas > 0:
                break
        except ValueError:
            pass

    while True:
        try:
            filas = int(input("Ingrese las dimensiones: "))
            if filas > 0:
                break
        except ValueError:
            pass
    
    n = filas*columnas
    matriz1 = np.zeros((columnas, filas)) # Matriz principal
    peru = input("Quien quiere que ingrese los numeros (Escriba MAQUINA o YO): ").upper()
    match peru:
        case "YO":
            for x in range(columnas):
                for i in range(filas):
                    eu = int(input(f"Ingrese el {x+1} numero: ")) # random.randrange(-9, 9) ESTE COMANDO ES PARA USARLO CON UN RANDOMIZADOR
                    matriz1[x, i] = eu
        case "MAQUINA":
            for x in range(n):
                while True:
                    eu = random.randrange(-9, 9) # ESTE COMANDO ES PARA USARLO CON UN RANDOMIZADOR
                    jaaj = True
                    while jaaj:
                        p = random.randrange(0, columnas)
                        k = random.randrange(0, filas)
                        if matriz1[p, k] == 0:
                            matriz1[p, k] = eu
                            jaaj = False
                        else:
                            pass
                    break

    print(matriz1, "\n")


    matriz2 = []; index = 0 
    for x in range(columnas):
        for i in range(filas):
            n = matriz1[x, i]
            if n != 0:
                matriz2.append([])
                matriz2[index] = [x, i, n]
                index += 1
   
    print(np.array(matriz2))
ejercicio3() # LLAMAR ASÍ AL EJERCICIO