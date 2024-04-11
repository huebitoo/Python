# Ejercicio 2
import numpy
import random


def ejercicio1():
    lista = numpy.array([int(input()) for x in range(12)]); print(lista); print(lista[::-1])


# Ejercicio 3
def ejercicio3():
    lista = numpy.array([random.randrange(-100, 100) for x in range(16)])
    a = sum(lista[:8]); print(a); b = sum(lista[8:]); print(b)


# Ejecicio 4
def ejercicio4():
    lista = numpy.array([random.randrange(-100, 100) for x in range(16)])
    print(lista); print(min(lista))


# Ejercicio 5
def ejercicio5():
    lista = numpy.array([random.randrange(-100, 100, 2) for x in range(16)])
    print(lista); print(numpy.amax(lista), lista.argmax()) # ARGMAX DESPLIEGA EL INDICE, AMAX EL MAXIMO.


# Ejercicio 6
def ejercicio6():
    lista = []; l = []; n = int(input("Dimensiones de la matriz: "))
    for x in range(n): 
        lista.append([])
        for i in range(n): lista[x].append(random.randrange(0, 9))
    for x in range(n):
        l.append([])
        for i in range(n): l[x].append(random.randrange(0, 9))
    l = numpy.array(l); print(l, "\n")
    lista = numpy.array(lista); print(lista, "\n")
    print(l+lista)

# Ejercicio 6.5 pro
def ejercicio6_5():
    lista = []; l = []; n = int(input("Dimensiones de la matriz: "))
    for x in range(n): 
        lista.append([])
        for i in range(n): lista[x].append(random.randrange(0, 9))
    for x in range(n):
        l.append([])
        for i in range(n): l[x].append(random.randrange(0, 9))
    l = numpy.array(l); print(l, "\n")
    lista = numpy.array(lista); print(lista, "\n")
    print(l*lista)

# Ejericio 7
def ejercicio7():
    lista = []; l = []; n = int(input("Dimensiones de la matriz: "))
    for x in range(n): 
        lista.append([])
        for i in range(n): lista[x].append(random.randrange(0, 9))
    for x in range(n):
        l.append([])
        for i in range(n): l[x].append(random.randrange(0, 9))
    l = numpy.array(l); print(l, "\n")
    lista = numpy.array(lista); print(lista, "\n")
    k = l*lista
    print(k, "\n")
    pe = 0
    for x in k:
        for i in range(n):
            if i == 0:
                t = numpy.sum(x)
                k[pe][i] = t
            else:
                k[pe][i] = k[pe][i-1]
        pe += 1
    print(k)

def ejercicio8():
    lista = []; l = []; n = int(input("Dimensiones de la matriz: "))
    for x in range(n): 
        lista.append([])
        for i in range(n): lista[x].append(random.randrange(0, 9))
    lista = numpy.array(lista); print(lista, "\n")
    lista = lista[::-1]
    print(lista)
