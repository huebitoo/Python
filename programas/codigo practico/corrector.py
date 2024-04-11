dic = ["este" , "es", "un", "diccionario", "que", "usaremos", "para", "corregir", "palabras", "erradas"]
palabra = ["nu", "dicionario", "palabras", "nueva", "korregir", "esste"]



def eyou(palabra, dic):
    suma = 0
    for x in dic:
        suma = 0
        for t in palabra:
            if t in x:
                suma += 1
            else:
                pass
            if suma >= (len(palabra)-1) and suma != 0:
                k = f"{palabra} es parecida a {x}"
                return k
    k = f"{palabra} no está en el diccionario"
    return k


t = True
p = 0
while t:
    t += 1
    k = palabra[p]
    palabra[p] = eyou(k, dic)
    if t == (len(palabra)+1):
        t = False
    p += 1

for x in palabra:
    print(x, "\n")