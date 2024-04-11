número = int(input("Ingrese el número: "))
aux = número
respaldo = 0
aux1 = número

while número < 0:
    número = int(input("Ingrese el número: "))


while aux1 > 0:
    aux1 = aux1 -1
    if número%aux == 0:
        respaldo = respaldo + aux
        aux = aux-1
    elif número%aux != 0:
        aux = aux-1

respaldo = respaldo - número

if número == respaldo:
    print(número, "es un número perfecto")
else:
    print(número, "no es un número perfecto")