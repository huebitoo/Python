import random
import LIBRERIA_PRUEBA
import os

mensaje_exito = ["¡Buen tiro!" , "¡Acertaste!", "En el blanco!", "¡Ataque exitoso!"]
mensaje_pesimo = ["¡Asqueroso!", "¡Retirate!", "¡Fuuas que asco!", "¡No le diste!"]


def mapa(x): # NUMEROS DEL MAPA
    a = '    '
    for b in range(x):
        if b >= 10:
            a += f'{b + 1}   '
        else:
            a += f'{b + 1}    '
    print(a)


def validar(min, Max, txt):
    x = input(txt)
    peru = True
    while peru:
        try:
            x = int(x)
            if int(x) > Max or int(x) < min:
                x = input(txt)
            else:
                x = int(x)
                peru = False
        except ValueError:
            x = input(txt)
    return x


# def repuesto(min, Max, txt): # VALIDACION DE LOS NUMEROS ¡¡¡¡USAR POR SI ACASO!!!!
#     x = input(txt)
#     while x > Max or x < min: # BUCLE DE COMPROBACION
#         x = input(txt) # PEDIR DE NUEVO
#     return x #RETURNAR

def validirec(): # VALIDACION DE LA DIRECCION
    x = input("Barco en vertical 'V' u horizontal 'H': ").upper() # INGRESAMOS VALOR
    while x != "V" and x != "H": # BUCLO DE COMPROBACION
        x = input("Barco en vertical 'V' u horizontal 'H': ").upper() # PEDIR DE NUEVO
    return x # RETURNAR


def casillas(n): # TABLERO
    total = []
    for x in range(n): # CICLO PARA LA CREACION DE MATRIS ANIDADA
        total.append([]) # MATRIS ANIDADA
        for j in range(n): # CREACION DE LISTA PARA MATRIS
            total[x].append("~") # AGREGAR "~" A LA LISTA PARA LAS MATRICES
    return total # RETURNAR


def barco(n, k, largo): # JUGADOR 1
    b1 = [] # GUARDAR COORDENADAS DE LOS BARCOS.
    for x in range(k): # CICLO PARA TODOS LOS BARCOS
        direc = validirec() # DIRECCION DE LOS BARCOS
        match direc:
            case 'V':
                coordx = validar(1, largo, "Ingrese coordenada x: ") # COLOCAMOS EL EJE X Y VALIDAMOS   
                coordy = validar(1, (largo-1), "Ingrese coordenada y: ") # COLOCAMOS EL EJE Y PARA LUEGO VALIDAR
                while True:
                    if (n[coordy][coordx-1] != "X") and (n[coordy-1][coordx-1] != "X") and (n[coordy - 2][coordx-1] != "X") and (coordy > 1) and (coordy < largo-1):
                        n[coordy-1][coordx-1] = "X"
                        n[coordy][coordx-1] = "X"
                        n[coordy - 2][coordx-1] = "X"
                        junto = str(coordx-1) + str(coordy-1) + str(coordx-1) + str(coordy) + str(coordx-1) + str(coordy-2)
                        b1.append(junto)
                        break
                    else:
                        coordx = validar(1, largo, "Ingrese coordenada x: ") 
                        coordy = validar(1, largo, "Ingrese coordenada y: ") 


            case 'H':
                coordx = validar(1, (largo-1), "Ingrese coordenada x: ") 
                coordy = validar(1, largo, "Ingrese coordenada y: ") 
                while True:
                    if (n[coordy-1][coordx] != "X") and (n[coordy-1][coordx-1] != "X") and (n[coordy-1][coordx - 2] != "X") and (coordx > 1) and (coordx <= largo-1):
                        n[coordy-1][coordx-1] = "X"
                        n[coordy-1][coordx] = "X"
                        n[coordy-1][coordx-2] = "X"
                        junto = str(coordx-1) + str(coordy-1) + str(coordx) + str(coordy-1) + str(coordx-2) + str(coordy-1) + "barco hundido"
                        b1.append(junto)
                        break
                    else:
                        coordx = validar(1, largo, "Ingrese coordenada x: ") 
                        coordy = validar(1, largo, "Ingrese coordenada y: ")    
    os.system("cls")
    juanfe = 1
    mapa(largo)
    for x in n:
        print(juanfe, x)
        juanfe += 1
    return n, b1


def barcocompu(n, k, largo): # JUGADOR 2 COMPUTADOR
    p = ["V", "H"]
    b2 = []
    for x in range(k):
        direc = random.choice(p)
        match direc:
            case 'V':
                coordx = random.randrange(1, largo)
                coordy = random.randrange(1, largo)
                while True:
                    if (n[coordy][coordx-1] != "X") and (n[coordy-1][coordx-1] != "X") and (n[coordy - 2][coordx-1] != "X") and (coordy > 1) and (coordy < largo-1):
                        n[coordy-1][coordx-1] = "X"
                        n[coordy][coordx-1] = "X"
                        n[coordy - 2][coordx-1] = "X"
                        junto = str(coordx-1) + str(coordy-1) + str(coordx-1) + str(coordy) + str(coordx-1) + str(coordy-2) + "barco hundido"
                        b2.append(junto)
                        break
                    else:
                        coordx = random.randrange(1, largo-1)
                        coordy = random.randrange(1, largo-1)


            case 'H':
                coordx = random.randrange(1, largo-1) 
                coordy = random.randrange(1, largo-1) 
                while True:
                    if (n[coordy-1][coordx] != "X") and (n[coordy-1][coordx-1] != "X") and (n[coordy-1][coordx - 2] != "X") and (coordx > 1) and (coordx < largo-1):
                        n[coordy-1][coordx-1] = "X"
                        n[coordy-1][coordx] = "X"
                        n[coordy-1][coordx-2] = "X"
                        junto = str(coordx-1) + str(coordy-1) + str(coordx) + str(coordy-1) + str(coordx-2) + str(coordy-1) + "barco hundido"
                        b2.append(junto)
                        break
                    else:
                        coordx = random.randrange(1, largo-1)
                        coordy = random.randrange(1, largo-1)
    return n, b2


#                                                 ------------------------JUEGO------------------------


n = validar(10, 1000, "Dimensiones tablero: ")
k = validar(2, n, "Numero de barcos: ")
k2 = k
os.system("cls")

#                                                                  JUGADOR 1

Mapa1 = casillas(n)
Mapa11, ubic1 = barcocompu(Mapa1, k, n)

#                                                           JUGADOR 2 (COMPUTADORA)

Mapa2 = casillas(n)
Mapa22, ubic2 = barcocompu(Mapa2, k2, n)


#                                                                ATAQUE

pepe = 1
juegoactivo = True


a = LIBRERIA_PRUEBA.validarini()
match a:
    case "JUGADOR":
        while juegoactivo:
            for turno in range(10**1000):
                if turno%2 == 0: # TURNO JUGADOR 1
                    Mapa22, k = LIBRERIA_PRUEBA.ataquecompu(Mapa22, ubic2, n, k) 
                    if k == 0:
                        print("¡¡Ganaste!!")
                        juegoactivo = False
                        break
                else:
                    Mapa11, k2 = LIBRERIA_PRUEBA.ataquecompu(Mapa11, ubic1, n, k2)
                    if k2 == 0:
                        print("¡¡Gano enemigo!!")
                        juegoactivo = False
                        break
                    else:
                        print("\n")
                        mapa(n)
                        pepe = 1
                        for pe in Mapa11:
                            print(pepe, pe)
                            pepe += 1
    case "COMPUTADOR":
        while juegoactivo:
            for turno in range(10**1000):
                if turno%2 == 0: # TURNO JUGADOR 1
                    Mapa11, k2 = LIBRERIA_PRUEBA.ataquecompu(Mapa11, ubic1, n, k2)
                    if k2 == 0:
                        print("¡¡Gano enemigo!!")
                        juegoactivo = False
                        break
                else:
                    Mapa22, k = LIBRERIA_PRUEBA.ataquecompu(Mapa22, ubic2, n, k) 
                    if k == 0:
                        print("¡¡Ganaste!!")
                        juegoactivo = False
                        break
                    else:
                        print("\n")
                        mapa(n)
                        pepe = 1
                        for pe in Mapa11:
                            print(pepe, pe)
                            pepe += 1
