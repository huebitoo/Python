x = int(input("Ingrese numero de integrantes: "))

while x < 0:
    x = int(input("Ingrese numero de integrantes validos: "))

precio = 0
for x in range(x):
    personas = int(input(f"Ingrese la edad de la persona {x+1}: "))
    
    while personas < 0 or personas >= 90:
        personas = int(input(f"Ingrese la edad de la persona {x+1} valida: "))
    
    if personas < 4:
        precio += 0
    elif personas >= 4 and personas < 18:
        precio += 5000
    elif personas >= 18 and personas < 65:
        precio += 10000
    else:
        precio += 3000

print(f"El precio total es: ${precio}")