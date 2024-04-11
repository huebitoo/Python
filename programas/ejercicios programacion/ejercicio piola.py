lista = []
n = 0 
m = int(input("Numeros de la lista: ")) # Cantidad nÃºmero de la lista
num = []
p = 0

for a in range(m):
    n = int(input(f"{a+1} Numero: "))
    lista.append(n)

n = int(input("El numero que quieres encontrar: ")) # Definir que numero existe para que sumado con otro de la misma lista, de este numero numero

for x in lista:
    if p == n:
        break
    for c in lista:
        if p == n:
            break
        elif x + c == n:
            if lista.index(x) != lista.index(c):
                p = x+c
                num.append(lista.index(x))
                num.append(lista.index(c))
                break
print(num)