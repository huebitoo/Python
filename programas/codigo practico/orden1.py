# EJERCICIO 3
nombre = []
lista = []

while True:
    nombre.append(input("Ingrese letras: "))
    if nombre[-1] == '':
        nombre.remove('')
        break

lista = nombre.copy()
lista.sort()
nombre.remove(lista[0])
nombre.insert(0, lista[0])
print(nombre)

