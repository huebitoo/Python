import os

def validar():
    num = input("Ingrese un número: ")
    while True:
        try:
            num = int(num)
            if num > 0 or num < 10:
                return num
            else:
                num = input("Ingrese un número válido: ")
        except ValueError:
            num = input("Ingrese un número válido: ")


def tablero():
    tablero = []
    for x in range(6): # TABLERO
        tablero.append([])
        for i in range(6):
            tablero[x].append("~")
    return tablero

def validart(tablero, x, i):
    a = 0
    while True:
        num = validar()
        for j in range(6):
            if tablero[j][i] != num and tablero[x][j] != num:
                pass
            else:
                print("No se puede este número, intente otro")
                break
            a += 1
        if a == 6:  
            tablero[x][i] = num
            return tablero
        else:
            pass
            a = 0


tableroo = tablero() # TABLERO 6X6

for x in range(6):
    for i in range(6):
        tableroo = validart(tableroo, x, i)
        print("cls")
        for t in tableroo:
            print(t)
print("¡¡Ganaste!!")




