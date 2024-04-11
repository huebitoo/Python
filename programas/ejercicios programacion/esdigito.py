def esdigito(x):
    k = True
    while k:
        x = x.replace('-', '', 1).replace('.', '', 1).replace(',', '', 1)
        x = x.isdigit()
        if x is True:
            k = False
            return x
        else:
            x = input("No contiene solo numeros, ingrese nuevamente: ")

x = input("Hola: ")
print(esdigito(x))