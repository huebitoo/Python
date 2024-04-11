import random
import os


def validar(largo, txt):
    x = input(txt)
    while not x.isdigit() or (int(x) < 0) or (int(x) > largo):
        x =input(txt)
    x = int(x)
    return x


def ataque(MapaEnemigo, coorde, largo, barcos, mensajeexito, mensajepesimo): #IMPLEMENTAR ATAQUE
    x = validar(largo, "Ingrese coordenada 'x' para atacar: ")
    y = validar(largo, "Ingrese coordenada 'y' para atacar: ")
    while MapaEnemigo[y-1][x-1] == "-" or MapaEnemigo[y-1][x-1] == "O":
        x = validar(largo, "Ingrese coordenada 'x' para atacar: ")
        y = validar(largo, "Ingrese coordenada 'y' para atacar: ")
    if (MapaEnemigo[y-1][x-1] == "X"):
        MapaEnemigo[y-1][x-1] = "O"
        os.system("cls")
        print(random.choice(mensajeexito))
        eu = str(x-1)+str(y-1)
        for eyou in coorde:
            if eu in eyou:
                coorde[coorde.index(eyou)] = coorde[coorde.index(eyou)].replace(eu, "")
                break
        for r in range(barcos):
            if coorde[r] == "barco hundido":
                barcos -= 1
                coorde[r] = ""
                os.system("cls")
                print("¡¡BARCO HUNDIDO!!")
    else:
        MapaEnemigo[y-1][x-1] = "-"
        os.system("cls")
        print(random.choice(mensajepesimo))
    
    return MapaEnemigo, barcos


def ataquecompu(MapaEnemigo, coorde, largo, barcos): #IMPLEMENTAR ATAQUE
    x = random.randrange(1, largo)
    y = random.randrange(1, largo)
    while MapaEnemigo[y-1][x-1] == "-" or MapaEnemigo[y-1][x-1] == "O":
        x = random.randrange(1, largo)
        y = random.randrange(1, largo)
    if (MapaEnemigo[y-1][x-1] == "X"):
        MapaEnemigo[y-1][x-1] = "O"
        print(" \n ¡¡¡ATAQUE ENEMIGO EXITOSO!!!")
        eu = str(x-1)+str(y-1)
        for eyou in coorde:
            if eu in eyou:
                coorde[coorde.index(eyou)] = coorde[coorde.index(eyou)].replace(eu, "")
                break
        for r in range(barcos):
            if coorde[r] == "barco hundido":
                barcos -= 1
                coorde[r] = "" # coorde[r].replace("barco hundido", "") # hola
                print("Barco aliado hundido!!")
    else:
        MapaEnemigo[y-1][x-1] = "-"
    
    return MapaEnemigo, barcos


def validarini():
    t = True
    while t:
        x = input("¿Quién va a empezar? ").upper()
        if x == "COMPUTADOR" or x == "JUGADOR":
            return x
        else:
            x = input("¿Quién va a empezar?").upper()


