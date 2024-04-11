list1 = [1,2]
list2 = [2]
num1 = ""
num2 = ""
x = len(list1)
y = len(list2)
a = x
b = y

while x != 0:
    num1 += str(list1[a-1])
    a -= 1
    x -= 1
while y != 0:
    num2 += str(list2[b-1])
    b -= 1
    y -= 1
num1 = num1[::-1]
num2 = num2[::-1]
resultado = int(num1) + int(num2)
resultado = str(resultado)
resultado = int(resultado[::-1])
resultadof = []
hola = resultado

k = resultado 
if k == 0:
    resultadof.append(resultado)
elif k != 0:
    while k != 0:
        j = resultado%10
        resultadof.append(j)
        k = k//10
        resultado = resultado//10

resultadof = resultadof[::-1]
print(resultadof)