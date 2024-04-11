import math 
punto1 = []
punto2 = []
punto3 = []
punto4 = []

a = 3
b = 0

while a != 0:
    b = int(input("Ingrese las coordenadas del punto 1: "))
    punto1.append(b)
    a -= 1
a = 3
while a != 0:
    b = int(input("Ingrese las coordenadas del punto 2: "))
    punto2.append(b)
    a -= 1
a = 3
while a != 0:
    b = int(input("Ingrese las coordenadas del punto 3: "))
    punto3.append(b)
    a -= 1
a = 3
while a != 0:
    b = int(input("Ingrese las coordenadas del punto 4: "))
    punto4.append(b)
    a -= 1

d1_2 = math.sqrt((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2 + (punto1[2] - punto2[2])**2)
dp1_2 = math.sqrt((punto3[0] - punto4[0])**2 + (punto3[1] - punto4[1])**2 + (punto3[2] - punto4[2])**2)
dpf = abs(d1_2-dp1_2)

print(d1_2, dp1_2, dpf)