fa = [] # lista de los fa
numero_temp = 0 # la cantidad de temperaturas que vamos a colocar
a = 0 # la temperatura que colocamos
celsius = [] # lista de los celsius

numero_temp = int(input("Ingrese la cantidad de temperaturas a cambiar: ")) # llamamos a la variable numeros e ingresamos la cantidad de numeros

for numero in range(numero_temp): # vamos a crear un rango con la cantidad de numeros de temperatura
    a = int(input("Ingrese temperatura en celsius: "))
    celsius.append(a) # de esta manera se agrega un número a una lista

for x in celsius: # por cada grado celsius, debemos recorrer la lista y evaluar cada valor por separado
    fa.append(round((x-32)*5/7)) # recorremos un numero por uno de la lista celsius y la transformamos

print("la temperatura final es ", fa) # imprimir el numero 