a = [2, 5, 4, 3, 5, 5, 2, 3, 1, 2, 5, 5, 3, 5]; a.sort()
p = 0; contador = 0; contador2 = 0; t = 0

for x in a:
    if x == a[t]:
        contador += 1
        k = x
    else:
        contador2 += 1
        if contador <= contador2:
            contador = contador2
            contador2 = 0
            t = p
        elif x == a[p-1]:
            pass
        else:
            contador2 = 1
    p += 1

print(f"La moda es {k} y se repite {contador} veces")