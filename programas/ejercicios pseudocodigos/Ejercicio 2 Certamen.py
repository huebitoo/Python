a = int(input("Autos: "))
m = int(input("Minutos: "))
n = m
p = 0
q = 0
o = m*a
aux = 0

while a < 0 or m < 0:
    a = int(input("Autos: "))
    m = int(input("Minutos: "))

while n != 0:
    p = int(input("Vehiculos: "))
    q = q + p
    n = n-1

if o > q:
    print("0 Vehiculos.")

elif o < q:
    aux = q-o
    print(aux, "Vehiculos")

elif o == q:
    print("0 Vehiculos")
