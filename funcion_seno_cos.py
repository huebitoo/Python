# NUMERO NARCISISTA ES QUE LA SUMA DE LOS DIGITOS ELEVADOS A LA CANTIDAD DE DIGITOS ES IGUAL AL NUMERO EJEMPLO EL NUMERO 153


def narcisista(numero):
    numero = str(numero)
    narcisista = 0
    narcisista = sum((int(i)**len(numero) for i in numero)) # ES UNA LISTA DE COMPRESION
    return narcisista == int(numero)


print(narcisista(153))