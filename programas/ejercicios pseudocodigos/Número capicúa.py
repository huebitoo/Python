a = int(input("Número: "))
m = 0
c = a
b = a
n = 0

while a < 10 or a > 10**10:
    a = int(input("Número: "))

while c != 0:
    m = m+1
    c = c//10

while b != 0:
    n = n + (b%10)*10**m
    b = b//10
    m = m-1

n = n//10

if n == a:
    print(a, "Es capicúa")
else:
    print(a, "No es capicúa")