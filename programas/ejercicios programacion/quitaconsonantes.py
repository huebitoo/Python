def quitarcosonante(x):
    consonante = "qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM"
    p = 0
    for a in x:
        if a in consonante:
            x = x.replace(x[p],"*", 1)
            p += 1
        else:
            p += 1
            pass
    print (x)
m= input()
quitarcosonante(m)