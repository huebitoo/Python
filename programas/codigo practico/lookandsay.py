n = input("Coloca el número: ")
k = input("veces a repetir: ")



a = []; a.append(n); pe = []
contador = 0; j = 0; je = 0
print(a)

for x in range(int(k)):
    if len(a) == 1:
        pe.append("1"); pe.append(n)
    else:
        for t in a:
            contador += 1
            je += 1
            if je == len(a):
                break
            else:
                pass
            if t != a[je]:
                pe.append(str(contador)); pe.append(a[j])
                j += 1
                contador = 0           
        if contador > 0:
            pe.append(str(contador)); pe.append(a[-1])
    print(pe)
    a = pe; pe =[]
    contador = 0; j = 0; je = 0