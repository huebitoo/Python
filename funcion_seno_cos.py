def factorial(numero):
    resultado = 1
    if numero == 0:
        return 1
    else : 
        for i in range(1, numero+1):
            resultado *= i
    return resultado

def seno(angulo, iteraciones):
    resultado = 0
    angulo = angulo * (3.1416)/180
    
    for i in range(iteraciones):
        resultado_antes = (((-1)**i) * angulo**(2*i+1))
        resultado_antes /= factorial(2*i+1)
        resultado += float(resultado_antes)
    return resultado

def coseno(angulo, iteraciones):
    resultado = 0
    angulo = angulo * (3.1416)/180
    
    for i in range(iteraciones):
        resultado_antes = (((-1)**i) * angulo**(2*i))
        resultado_antes /= factorial(2*i)
        resultado += float(resultado_antes)
    return resultado



for i in range(1, 30):
    print(f"Iteracion {i}: {seno(30, i)}")
    
    
for i in range(1, 30):
    print(f"Iteracion {i}: {coseno(60, i)}")