def fibunacci(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibunacci(n-1) + fibunacci(n-2)


for x in range(20): # Cuantos numeros de fibunacci quiero
    print(fibunacci(x))


# METODO CON WHILE
a = 0
b = 1
c = 1
i = 0
while (i < 10):
    c = a + b
    a = b
    b = c
    i += 1
    print(c)