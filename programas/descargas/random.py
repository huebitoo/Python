# Creemos una lista 

lista = []

while True:
    a = int(input("Ingrese un número: "))
    if a == 0 : break
    lista.append(a)

for i in range(len(lista) - 2):
    if lista[i] > lista[i + 1] > lista[i + 2]:
        print("Decreciente")
    elif lista[i] < lista[i + 1] < lista[i + 2]:
        print("Creciente")
    elif lista[i] == lista[i + 1] == lista[i + 2]:
        print("Plano")
    elif lista[i] < lista[i + 1] > lista[i + 2]:
        print("Cumbre")

