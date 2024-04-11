# DA VINCI LISTO!!
def validar():
    t = True
    while t:
        num = input("Ingrese los numeros separados por espacios: ")
        if num.replace(" ", "").isdigit() == False:
            num = input("Ingrese los numeros separados por espacios: ")
        else:
            t = False
    return num


def fibunaccisu(fibunacci):
    a = 0
    b = 1
    c = 0
    p = 0
    while p < 100:
        c = a + b
        fibunacci.append(c)
        a = b
        b = c
        p += 1
    return fibunacci


def validartxt():
    t = True
    while t:
        num = input("Ingrese texto: ")
        if len(num) > 100 or len(num) < 1:
            num = input("Ingrese texto: ")
        else:
            t = False
    return num


fibunacci = []; fibunacci = fibunaccisu(fibunacci) # [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657]
usar = []
numeros = validar() # "34 21 13 144 1597 3 987 610 8 5 89 2 377 2584 1"
texto = validartxt(); texto = texto.replace(",", "").replace("!", "").replace("'", "").replace(" ", "").replace('"', "")  # "O, DRACONIAN DEVIL!"

a = ""; p = 0; num = []
xd = []
y = ""


for x in range(len(texto)*2):
    usar.append("-")


for x in numeros:
    p += 1 
    if x != " ":
        a += x
    else:
        xd.append(int(a))
        a = ""
    if p == len(numeros):
        xd.append(int(a))


for x in range(len(xd)):
    if not fibunacci[x] in xd:
        num.append(fibunacci[x])


for x in texto:
    for t in xd:
        j = fibunacci.index(int(t))
        usar[j] = x
        xd.remove(t)
        break


for x in num:
    j = fibunacci.index(x)
    usar[j] = " "


while "-" in usar:
    usar.remove("-")


for x in usar:
    y += x
print(y)