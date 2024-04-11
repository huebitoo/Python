n = int(input("Numero de productos: "))
a = []

for x in range(n):
    a.append(input(f"{x+1} producto: "))

a.sort()
print(a)