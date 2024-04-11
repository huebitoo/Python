n = int(input("Numero de pelotas: "))

while n < 0 or n > 1000: #DEFINIMOS EL NUMERO DE PELOTAS
    n = int(input("Numero de pelotas: "))

radio = int(input("Radio de la pelota: "))

while radio < 0 or radio > 100: #DEFINIMOS EL RADIO CON LOS PARAMETROS
    radio = int(input("Radio de la pelota: "))
a = 0
b = 100
c = n

while c > 1:
    if radio == b:
        a = a+1
        c = c-1
        radio = int(input("Radio de la pelota: "))
    elif radio < b:
        a = 1
        b = radio
        c = c-1
        radio = int(input("Radio de la pelota: "))
    elif radio > b:
        c = c-1
        radio = int(input("Radio de la pelota: "))
        
while c == 1:
    if radio == b:
        a = a+1
        c = c-1
    elif radio < b:
        a = 1
        b = radio
        c = c-1
    elif radio > b:
        c = c-1

else:
    print("Se produjeron", a, "pelotas de radio ", b)