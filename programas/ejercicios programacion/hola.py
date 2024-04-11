T=[]; n= int(input("Ingrese la cantidad de productos: "))
while n < 2: n= int(input("Error ingrese numero mayor a 1 : "))
for i in range(n): T.append(input(f"Ingrese nombre del producto N°{i+1}: ")); T.sort(); print(T)



