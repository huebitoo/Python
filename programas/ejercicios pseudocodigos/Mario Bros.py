NM = int(input("Saltos: "))
SA = 0
SB = 0
k = 0
n = NM
p = 0


while 0 > NM or NM > 50:
    NM = int(input("Saltos: "))
k = int(input("Altura inicial: "))

while n > 0:
    p = int(input("Altura muralla: "))
    if p > k:
        SA = SA + 1
        n = n-1
        k = p
    elif p == k:
        n = n - 1
    elif p < k:
        SB = SB + 1
        n = n - 1

print("Saltos altos:", SA, "y saltos bajos:", SB)

