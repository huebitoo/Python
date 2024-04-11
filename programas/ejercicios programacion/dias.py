a = input("Coloque el dia/mes/año en que nacio en ese orden respectivo: ")
a = a.split("/")
b = input("Fecha actual (mismo formato): ")
b = b.split("/")

año = int(b[2])-int(a[2])
mes = int(b[1])-int(a[1])
dias = int(b[0])-int(a[0])

total = (año*365)+(mes*30)+dias
print(f"La cantidad de días que ha vivido son {total} días.")

