javier = [x for x in range(10000) if x != 0]
contador_general = 1

for x in javier:
    contador = 0
    for i in range(x):
        if i == 0:
            pass
        elif x%i == 0:
            contador += 1
    if contador == 1:
        contador_general += 1
        print(f"{contador_general}: Primo {x}")

