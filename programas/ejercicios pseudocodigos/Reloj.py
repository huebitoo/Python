h = int(input("Hora: "))
m = int(input("Minutos: "))
k = int(input("Minutos extra: "))
d = 0
s = 0
mes = 0

while h > 23 or h < 0:
    h = int(input("Hora: "))

while m > 60 or m < 0:
    m = int(input("Minutos: "))

if k+m >= 60:
    m = m+k
    while m >= 60:
        m = m-60
        h = h+1
    while h > 23:
        d = d+1
        h = h-24
    while d > 6:
        d = d-7
        s = s+1
    while s > 3:
        s = s-4
        mes = mes+1


print(mes, "meses,", s, "semanas,", d, "días,", h,"horas,", m,"minutos.")