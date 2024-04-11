decimal = int(input("Número: ")) #INTRODUCIR EL NÚMERO
binario = "" #PARA QUE NO LO LEA COMO INT, SINO COMO STRING
aux = 0

#VALIDAR SI EL DECIMAL ES POSITIVO
while decimal < 0:
    decimal = int(input("Número: "))

#TRANSFORMACION DE DECIMAL A BINARIO
while decimal > 0:
    aux = decimal%2 #GUARDAMOS EL RESTO EN UNA VARIABLE AUXILIAR
    binario += str(aux) #TRANSFORMAMOS EL AUX EN STRING PARA QUE NO SE SUME, SINO SE AGRUPE
    decimal = decimal//2 #DIVIDIMOS EN EL FACTOR 2

print(binario)