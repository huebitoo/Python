c = int(input("Consultas: "))
aux = c

while c < 0 or c > 100:
    c = int(input("Consultas: "))

x = 0 # frontera x
y = 0 #frontera y

while aux > 0:
    x1 = int(input("Latitud: "))
    y1 = int(input("Longitud: "))
    while x1 < -1000 or x1 > 1000:
        x1 = int(input("Latitud: "))
    while y1 < -1000 or y1 > 1000:
        y1 = int(input("Longitud: "))
    
    if x1 == x or y1 == y:
        print("Frontera")
        aux = aux - 1
    elif x1 > x and y1 > y:
        print("Noreste")
        aux = aux - 1
    elif x1 > x and y1 < y:
        print("Sureste")
        aux = aux - 1
    elif x1 < x and y1 > y:
        print("Noroeste")
        aux = aux - 1
    elif x1 < x and y1 < y:
        print("Suroeste")
        aux = aux - 1
