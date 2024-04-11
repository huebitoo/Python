nom = [] # ["pato", "lisa", "pata", "pita", "pisa"] # ["remar", "pitos", "remas", "remos", "retos", "ritos"]
num = int(input("Ingrese numero de palabras: "))
largo = int(input("Largo palabras: "))


for x in range(num):
    palabra = input(f"Ingrese palabra {x+1}: ")
    while not len(palabra) == largo:
        palabra = input(f"Ingrese palabra {x+1}: ")
    nom.append(palabra)
nomm = []; nomm.append(nom[0])


def detectar(nom, nomm):
    suma = 0
    if len(nom) > 1:
        nom.remove(nomm[-1])
    else:
        nom.remove(nomm[-1])
        return nom, nomm
    for x in nom:
        for t in x:
            if t in nomm[-1]:
                suma += 1
            else:
                pass
        if suma >= (len(nom[0])-1):
            nomm.append(x)
            suma = 0
            break
        else:
            suma = 0
    return nom, nomm


t = True
while t:
    nom, nomm = detectar(nom, nomm)
    if len(nom) == 0:
        t = False
print(nomm)