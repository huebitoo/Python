def leevalida(m,M,txt):
    while True:
        try:
            x=int(input(txt))
            while x<m or x>M:
                print("error")
                x=int(input(txt))
        except ValueError:
            print("Ingresar un valor valido")
        else:
            break
    return x

def validcoords(txt):
    while True:
        xy=((input(txt)).strip("()")).split(",")
        if all(ele.isdigit() for ele in xy) and len(xy)==2:
            return [int(xy[0])-1,int(xy[1])-1]

def Crear_Mapa(largo):
    map=[]
    newlist=[]
    for k in range(largo):
        newlist.append('~')
    for i in range(largo):
        map.append(newlist)
    return map

def CrearBarcos(cantidad,bounds):
    barcos=[]
    for i in range(cantidad):
        while True:
            
            seleccion=input("¿Barco en horizontal(h) o vertical(v)? ")
            if seleccion=="v":
                while True:
                    xy=validcoords("Ingresar coordenadas del barco: ")
                    y=int(xy[1])
                    down=[xy[0],(y+1)]
                    up=[xy[0],(y-1)]
                    if y>=1 and y<=bounds-2 and xy not in barcos and up not in barcos and down not in barcos:                    
                        barcos.append(up)
                        barcos.append(xy)
                        barcos.append(down)
                        break  
                break
                
            elif seleccion=="h":
                while True:
                    xy=validcoords("Ingresar Coordenadas: ")
                    x=int(xy[0])                    
                    right=[x+1,xy[1]]
                    left=[x-1,xy[1]]
                    if x>=1 and x<=bounds-2 and xy not in barcos and right not in barcos and left not in barcos:
                        barcos.append(right)
                        barcos.append(xy)                                
                        barcos.append(left)
                        break
                break
            
    return barcos

def actualizar_mapa(icon,map,coord):
    newmap=[]
    x=int(coord[0])
    newmap+=map[0:x]+[icon]
    print(newmap)
    map=newmap+map[x+1:]
    print(map)

    return map

def ordercoords(coords):
    neworder=sorted(coords , key=lambda k: [k[1]])
    return neworder

#Inicio

bounds=leevalida(10,1000,"Ingresa tamaño del tablero. NxN, N: ")
barcos=leevalida(2,bounds,"Ingresa la cantidad de naves: ")
lista_de_barcos=CrearBarcos(barcos,bounds)

print(lista_de_barcos)

mimapa=Crear_Mapa(bounds)
mapaenemigo=None


#Actualizar mapa
k=0
neomapa=[]

readablecoords=ordercoords(lista_de_barcos)
print(readablecoords)
for i in range(bounds):
    print(readablecoords[k])
    print(readablecoords[k][1])
    while i==int((readablecoords[k])[1]):
        neomapa.append(actualizar_mapa('0',mimapa[i],readablecoords[k]))
        k+=1
        if k+1==len(lista_de_barcos):
            break
    else:
        neomapa.append(mimapa[i])
        
print(neomapa)