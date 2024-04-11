while True:
    nombre = input("Ingrese un nombre: ")
    if len(nombre) > 12:
        print("El nombre debe tener como máximo de 12 letras/números")
    elif len(nombre) < 6:
        print("El nombre debe tener como minimo 6 letras/números")
    for x in nombre:
        suma = 0
        if x in "0123456789":
            suma += 1
        else:
            pass
    if suma > 0:
        print(True)
    else:
        print("Debe contener números")