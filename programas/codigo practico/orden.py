# EJERCICIO 2
nombre = []
lista = []

while True:
    nombre.append(input("Ingrese nombres: "))
    if nombre[-1] == "":
        break

for x in nombre:
    if nombre[-2] == x:
        lista = lista[::-1]
        lista.append(x)
        lista = lista[::-1]
    else:
        lista.append(x)

lista.remove("")
print(lista)
