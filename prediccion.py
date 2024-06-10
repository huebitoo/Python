import random as r

def prediccion(texto, palabra, largo):
    texto = texto.lower().split()
    contador = 0
    lista_posibles = []
    for x in texto:
        if palabra == x:
            try:
                no_se_que = ""
                for i in range(largo):
                    num_index = texto.index(palabra)
                    no_se_que += texto[num_index + i] + " "
                lista_posibles.append(no_se_que)
                texto[contador] = ""
            except IndexError:
                pass
        contador += 1
    return lista_posibles

def posible(lista):
    x = r.randrange(0, len(lista))
    print(f"{lista[x]}")

lista = prediccion("", "mi", 5)
posible(lista)