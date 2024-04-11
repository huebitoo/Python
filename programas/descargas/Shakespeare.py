q = int(input("Ingrese cantidad de palabras: "))
while not q > 0:
    q = int(input("Cantidad de palabras fuera de rango, por favor reingrese número: "))
l = int(input("Ingrese cantidad de letras por palabra: "))
while not l > 0:
    l = int(input("Cantidad de letras por palabra fuera de rango, por reingrese número: "))

# Creación de lista con las palabras introducidas por el usuario
palabras = []
for x in range(q):
    palabra = input(f"Ingrese la palabra {x+1}: ").lower()
    while not len(palabra) == l:
        palabra = input(f"Largo de palabra incorrecto, por favor reingrese la palabra {x+1}: ").lower()
    palabras.append(palabra)

# Ordenamiento de las palabras segun su cantidad de cambios en las letras
cont = 0
palabras_final = [" " for x in range(q)]
cambio = 0
for palabra in palabras:
    for palabra_2 in palabras:
        cambio = 0
        if cont < q:
            index = 0
            for letra in palabra:
                if letra != palabra_2[index]:
                    cambio += 1
                    index += 1
                else:
                    index += 1
            palabras_final[cambio] = palabra_2
            cont += 1
for x in palabras_final:
    print(x)
        
